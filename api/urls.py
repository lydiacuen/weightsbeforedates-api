from django.urls import path
from .views.buffpost_views import BuffPostsView, BuffPostDetailView
from .views.user_views import SignUpView, SignInView, SignOutView, ChangePasswordView

urlpatterns = [
  	# Restful routing
    path('buffposts/', BuffPostsView.as_view(), name='buffposts'),
    path('buffposts/<int:pk>/', BuffPostDetailView.as_view(), name='buffpost_detail'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('change-pw/', ChangePasswordView.as_view(), name='change-pw')
]
