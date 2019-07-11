from django.db import transaction
from rest_framework import serializers

from tasks.models import Task
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

    def executor_select(self, instance, user):
        with transaction.atomic():
            if instance.accept:
                executor = instance.executor
                if executor is None:
                    Task.objects.select_for_update().filter(id=instance.id).update(
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

    def transfer_money(self, instance):
        with transaction.atomic():
            if instance.finished:
                instance.created_by.update_balance(instance.price, Transaction.WITHDRAWAL, instance.created_by)
                Transaction.objects.create(
                    user=instance.created_by,
                    action=Transaction.WITHDRAWAL,
                    amount=instance.price
                )
                instance.executor.update_balance(instance.price, Transaction.REPLENISH, instance.created_by)
                Transaction.objects.create(
                    user=instance.executor, 
                    action=Transaction.REPLENISH,
                    amount=instance.price
                )

    def update(self, instance, validated_data):
        super(TaskDoneSerializer, self).update(instance, validated_data)
        self.transfer_money(instance)
        return instance

    class Meta:
        model = Task
        fields = ('finished',)
