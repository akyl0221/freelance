from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import Transaction

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(
        queryset=User.objects.all(), message='This email is Exist')])

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'role', 'balance')


class UserLoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'role', 'balance')


class UserChangeBalanceSerializer(serializers.ModelSerializer):

    def transfer_execution(self, validated_data):
        user,  amount, action = \
            (validated_data.get('user'),
             validated_data.get('amount'),
             validated_data.get('action'),)
        user.update_balance(amount, action, user)

    def create(self, validated_data):
        super(UserChangeBalanceSerializer, self).create(validated_data)
        self.transfer_execution(validated_data)
        return validated_data

    class Meta:
        model = Transaction
        fields = ('id', 'user', 'action', 'amount', 'created_time', )

