from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.buffpost import BuffPost
from ..serializers import BuffPostSerializer

# Create your views here.

class BuffPostsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BuffPostSerializer

    def get(self, request):
        """Index request"""
        # Get all the buffposts:
        # buffposts = BuffPost.objects.all()
        # Filter the buffposts by owner, so you can only see your owned buffposts
        buffposts = BuffPost.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = BuffPostSerializer(buffposts, many=True).data
        return Response({'buffposts': data})

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['buffpost']['owner'] = request.user.id
        # Serialize/create buffpost
        buffpost = BuffPostSerializer(data=request.data['buffpost'])
        # If the buffpost data is valid according to our serializer...
        if buffpost.is_valid():
            # Save the created buffpost & send a response
            buffpost.save()
            return Response({'buffpost': buffpost.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(buffpost.errors, status=status.HTTP_400_BAD_REQUEST)


class BuffPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        # Locate the buffpost to show
        buffpost = get_object_or_404(BuffPost, pk=pk)
        # Only want to show owned buffposts?
        if request.user != buffpost.owner:
            raise PermissionDenied('Unauthorized, you do not own this buffpost')

        # Run the data through the serializer so it's formatted
        data = BuffPostSerializer(buffpost).data
        return Response({'buffpost': data})

    def delete(self, request, pk):
        """Delete request"""
        # Locate buffpost to delete
        buffpost = get_object_or_404(BuffPost, pk=pk)
        # Check the buffpost's owner against the user making this request
        if request.user != buffpost.owner:
            raise PermissionDenied('Unauthorized, you do not own this buffpost')
        # Only delete if the user owns the  buffpost
        buffpost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate BuffPost
        # get_object_or_404 returns a object representation of our BuffPost
        buffpost = get_object_or_404(BuffPost, pk=pk)
        # Check the buffpost's owner against the user making this request
        if request.user != buffpost.owner:
            raise PermissionDenied('Unauthorized, you do not own this buffpost')

        # Ensure the owner field is set to the current user's ID
        request.data['buffpost']['owner'] = request.user.id
        # Validate updates with serializer
        data = BuffPostSerializer(
            buffpost, data=request.data['buffpost'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
