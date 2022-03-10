from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.comment import Comment
from ..serializers import CommentSerializer

# Create your views here.


class CommentsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get(self, request):
        """Index request"""
        # Get all the comments:
        # comments = Comment.objects.all()
        # Filter the comments by owner, so you can only see your owned comments
        comments = Comment.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = CommentSerializer(comments, many=True).data
        return Response({'comments': data})

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['comment']['owner'] = request.user.id
        # Serialize/create comment
        comment = CommentSerializer(data=request.data['comment'])
        # If the comment data is valid according to our serializer...
        if comment.is_valid():
            # Save the created comment & send a response
            comment.save()
            return Response({'comment': comment.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        # Locate the comment to show
        comment = get_object_or_404(Comment, pk=pk)
        # Only want to show owned comments?
        if request.user != comment.owner:
            raise PermissionDenied(
                'Unauthorized, you do not own this comment')

        # Run the data through the serializer so it's formatted
        data = CommentSerializer(comment).data
        return Response({'comment': data})

    def delete(self, request, pk):
        """Delete request"""
        # Locate comment to delete
        comment = get_object_or_404(Comment, pk=pk)
        # Check the comment's owner against the user making this request
        if request.user != comment.owner:
            raise PermissionDenied(
                'Unauthorized, you do not own this comment')
        # Only delete if the user owns the  comment
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Comment
        # get_object_or_404 returns a object representation of our Comment
        comment = get_object_or_404(Comment, pk=pk)
        # Check the comment's owner against the user making this request
        if request.user != comment.owner:
            raise PermissionDenied(
                'Unauthorized, you do not own this comment')

        # Ensure the owner field is set to the current user's ID
        request.data['comment']['owner'] = request.user.id
        # Validate updates with serializer
        data = CommentSerializer(
            comment, data=request.data['comment'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
