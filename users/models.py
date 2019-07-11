from django.contrib.auth.models import AbstractUser
from django.db import models, transaction


class CustomUser(AbstractUser):
    CUSTOMER = 1
    EXECUTOR = 2

    ROLE = (
        (CUSTOMER, 'Customer'),
        (EXECUTOR, 'Executor'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE, default=CUSTOMER)

    balance = models.DecimalField('balance', max_digits=10, decimal_places=1, null=True, blank=True, default=0)
    
    def __str__(self):
        return self.email

    def update_balance(self, balance, reason, user):
        with transaction.atomic():
            if reason is Transaction.REPLENISH:
                CustomUser.objects.select_for_update().filter(id=user.id).update(
                    balance=user.balance + balance
                )
            elif reason is Transaction.WITHDRAWAL:
                CustomUser.objects.select_for_update().filter(id=user.id).update(
                    balance=user.balance - balance
                )


class Transaction(models.Model):
    REPLENISH = 1
    WITHDRAWAL = 2

    CHOICES = (
        (REPLENISH, 'Replenish'),
        (WITHDRAWAL, 'Withdrawal'),
    )

    user = models.ForeignKey(
        'CustomUser', related_name='balance_changes',
        on_delete=models.CASCADE
    )
    action = models.PositiveSmallIntegerField(choices=CHOICES, default=REPLENISH)
    amount = models.DecimalField('Amount', default=0, max_digits=18, decimal_places=6)
    created_time = models.DateTimeField(auto_now_add=True)

