from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserChangeBalance

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'role', 'balance')


class UserLoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'role', 'balance')


class UserChangeBalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserChangeBalance
        fields = ('id', 'from_user', 'reason', 'amount', 'datetime', 'to_user')

