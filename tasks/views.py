from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskCreateSerializer, TaskDetailSerializer, TaskListSerializer
from .permissions import CreateTask, IsOwnerOrReadOnly, ListTask


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = (IsAuthenticated, CreateTask,)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, ListTask,)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = (IsAuthenticated, CreateTask, IsOwnerOrReadOnly,)



