from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task

from tasks.serializers import \
    (TaskCreateDetailSerializer,
     TaskListSerializer,
     TaskAcceptSerializer,
     TaskDoneSerializer)

from tasks.permissions import \
    (CreateTask,
     IsOwnerOrReadOnly,
     ListTask,
     IsExecutorOrReadOnly)


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateDetailSerializer
    permission_classes = (IsAuthenticated, CreateTask,)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, ListTask,)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'PUT':
            serializer_class = TaskCreateDetailSerializer
        return serializer_class


class TaskAcceptView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'PUT':
            serializer_class = TaskAcceptSerializer
        return serializer_class


class TaskDoneView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'PUT':
            serializer_class = TaskDoneSerializer
        return serializer_class


class ExecutorAcceptedView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    permission_classes = (IsExecutorOrReadOnly, IsAuthenticated)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(executor=user.id)