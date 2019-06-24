from rest_framework import permissions
from rest_framework.permissions import BasePermission

from users.models import CustomUser


class CreateTask(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == CustomUser.CUSTOMER:
            return True
        return False


class ListTask(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            user = request.user
            if user.role == CustomUser.EXECUTOR:
                return True
        return False


class IsOwnerOrReadOnly(permissions.BasePermission):
     def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user


class IsExecutorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.executor == request.user