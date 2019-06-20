from django.contrib.auth.models import AbstractUser
from django.db import models, transaction
from django.db.models import F


class CustomUser(AbstractUser):
    CUSTOMER = 1
    EXECUTOR = 2

    ROLE = (
        (CUSTOMER, 'Customer'),
        (EXECUTOR, 'Executor'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE, default=CUSTOMER)

    balance = models.DecimalField('balance', max_digits=10, decimal_places=1, null=True, blank=True)
    
    def __str__(self):
        return self.email

    def update_balance(self, balance):
        with transaction.atomic():
            CustomUser.objects.select_for_update().filter(
                role=CustomUser.CUSTOMER).update(
                balance=F('balance') - balance
            )
            CustomUser.objects.select_for_update().filter(
                role=CustomUser.EXECUTOR).update(
                balance=F('balance') + balance
            )


class UserChangeBalance(models.Model):
    REPLENISH = 1
    WITHDRAWAL = 2
    PAY_WORK = 3

    CHOICES = (
        (REPLENISH, 'Replenish'),
        (WITHDRAWAL, 'Withdrawal'),
        (PAY_WORK, 'payment for work'),
    )

    user = models.ForeignKey('CustomUser', related_name='balance_changes', on_delete=models.CASCADE)
    reason = models.PositiveSmallIntegerField(choices=CHOICES, default=REPLENISH)
    amount = models.DecimalField('Amount', default=0, max_digits=18, decimal_places=6)
    datetime = models.DateTimeField(auto_now_add=True)







