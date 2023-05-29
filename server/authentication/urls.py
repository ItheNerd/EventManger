from django.urls import path
from authentication.views import RegisterView, LogoutView, CheckLoggedInUser
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from authentication.views import UserDetailView

urlpatterns = [
    path("", views.getRoutes),
    path("register/", RegisterView.as_view(), name="register"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("current-user/", CheckLoggedInUser.as_view(), name="some-view"),
]
