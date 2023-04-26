# api/views.py
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .serializers import UserSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class UserDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


