from django.db import transaction
from rest_framework import serializers

from .models import Task
from users.models import Transaction


class TaskCreateDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'price', 'created_time', 'created_by', 'executor')


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'price', 'created_time', 'created_by', 'executor', 'finished')


class TaskAcceptSerializer(serializers.ModelSerializer):

    def task_accepted(self, instanse, user):
        with transaction.atomic():
            if instanse.accept is True:
                executor = Task.objects.get(id=instanse.id).executor
                if executor is None:
                    Task.objects.select_for_update().filter(id=instanse.id).update(
                        executor=user.id
                    )

    def update(self, instance, validated_data):
        super(TaskAcceptSerializer, self).update(instance, validated_data)
        user = self.context['request'].user
        self.task_accepted(instance, user)
        return instance

    class Meta:
        model = Task
        fields = ('accept',)


class TaskDoneSerializer(serializers.ModelSerializer):

    def task_done(self, instanse):
        if instanse.finished is True:
            with transaction.atomic():
                Transaction.objects.create(
                    user=instanse.created_by, reason=Transaction.WITHDRAWAL,
                    amount=instanse.price
                )
                instanse.created_by.update_balance(instanse.price, Transaction.WITHDRAWAL, instanse.created_by)
                Transaction.objects.create(
                    user=instanse.executor, reason=Transaction.REPLENISH,
                    amount=instanse.price
                )
                instanse.executor.update_balance(instanse.price, Transaction.REPLENISH, instanse.created_by)

    def update(self, instance, validated_data):
        super(TaskDoneSerializer, self).update(instance, validated_data)
        self.task_done(instance)
        return instance

    class Meta:
        model = Task
        fields = ('finished',)

