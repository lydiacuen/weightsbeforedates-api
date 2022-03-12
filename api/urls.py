from django.urls import path
from .views.buffpost_views import BuffPostsView, BuffPostDetailView
from .views.profile_views import ProfileView, ProfileDetailView
from .views.user_views import SignUpView, SignInView, SignOutView, ChangePasswordView

urlpatterns = [
    # Restful routing
    path('buffposts/', BuffPostsView.as_view(), name='buffposts'),
    path('buffposts/<int:pk>/', BuffPostDetailView.as_view(), name='buffpost-detail'),
    path('buffposts/create/', BuffPostsView.as_view(), name='create-buffpost'),
    path('buffposts/<int:pk>/update/',
         BuffPostDetailView.as_view(), name='update-buffpost'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('change-pw/', ChangePasswordView.as_view(), name='change-pw'),
    path('profiles/', ProfileView.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profiles/create/', ProfileView.as_view(), name='create-profile'),
    path('profiles/<int:pk>/update/',
         ProfileDetailView.as_view(), name='update-profile')
]
