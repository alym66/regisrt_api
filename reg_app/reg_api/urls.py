# api/urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import UserRegistrationAPIView, UserDeleteAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('delete/', UserDeleteAPIView.as_view(), name='delete'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
]
