from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import serializers


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        token["email"] = user.email
        # ...

        return token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True
    )  # Mark password field as write-only

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
