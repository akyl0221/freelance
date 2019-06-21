from rest_framework import serializers

from .models import Task


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'price', 'created_time', 'created_by', 'executor')


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'price', 'created_time', 'created_by', 'executor', 'finished')


class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'price', 'created_time', 'created_by', 'executor', 'finished')

