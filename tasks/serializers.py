from rest_framework import serializers

from .models import Task


class TaskCreateSerializer(serializers.Serializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'price', 'created_time', 'created_by', 'executor')


class TaskDetailSerializer(serializers.Serializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'price', 'created_time', 'created_by', 'executor')

