from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.profile import Profile
from ..serializers import ProfileSerializer

# Create your views here.


class ProfileView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get(self, request):
        """Index request"""
        # Get all the profiless:
        # profiles = Profile.objects.all()
        # Filter the profiles by owner, so you can only see your owned profiles
        profiles = Profile.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ProfileSerializer(profiles, many=True).data
        return Response({'profiles': data})

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['profile']['owner'] = request.user.id
        # Serialize/create profile
        profile = ProfileSerializer(data=request.data['profile'])
        # If the profile data is valid according to our serializer...
        if profile.is_valid():
            # Save the created profile & send a response
            profile.save()
            return Response({'profile': profile.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(profile.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        # Locate the profile to show
        profile = get_object_or_404(Profile, pk=pk)
        # Only want to show owned profile?
        if request.user != profile.owner:
            raise PermissionDenied(
                'Unauthorized, you do not own this profile')

        # Run the data through the serializer so it's formatted
        data = ProfileSerializer(profile).data
        return Response({'profile': data})

    def delete(self, request, pk):
        """Delete request"""
        # Locate profile to delete
        profile = get_object_or_404(Profile, pk=pk)
        # Check the profile's owner against the user making this request
        if request.user != profile.owner:
            raise PermissionDenied(
                'Unauthorized, you do not own this profile')
        # Only delete if the user owns the  profile
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Profile
        # get_object_or_404 returns a object representation of our Profile
        profile = get_object_or_404(Profile, pk=pk)
        # Check the profile's owner against the user making this request
        if request.user != profile.owner:
            raise PermissionDenied(
                'Unauthorized, you do not own this profile')

        # Ensure the owner field is set to the current user's ID
        request.data['profile']['owner'] = request.user.id
        # Validate updates with serializer
        data = ProfileSerializer(
            profile, data=request.data['profile'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
