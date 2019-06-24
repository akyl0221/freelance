from django.contrib.auth import get_user_model , authenticate, login

from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import UserCreateSerializer, CustomUserSerializer, UserLoginSerializer, UserChangeBalanceSerializer
from .models import Transaction

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(views.APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, **serializer.validated_data)
            if user:
                login(request, user)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)


class UserChangeBalanceCreateView(generics.CreateAPIView):
    serializer_class = UserChangeBalanceSerializer
    permission_classes = (IsAuthenticated,)


class UserChangeBalanceListView(generics.ListAPIView):
    serializer_class = UserChangeBalanceSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user.id)


