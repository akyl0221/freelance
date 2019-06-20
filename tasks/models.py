from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='executor')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default='', related_name='task')

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return self.title


@receiver(post_save, sender=Task)
def task_post_save(sender, instance, **kwargs):
    instance.created_by.update_balance(instance.price)

