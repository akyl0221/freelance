from django.contrib.auth.models import AbstractUser
from django.db import models, transaction
from django.db.models import F
from django.dispatch import receiver
from django.db.models.signals import post_save


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

    def update_balance(self, balance, reason):
        with transaction.atomic():
            if reason == UserChangeBalance.REPLENISH:
                CustomUser.objects.select_for_update().update(
                    balance=F('balance') + balance
                )
            elif reason == UserChangeBalance.WITHDRAWAL:
                CustomUser.objects.select_for_update().update(
                    balance=F('balance') - balance
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


@receiver(post_save, sender=UserChangeBalance)
def balance_post_save(sender, instance, **kwargs):
    instance.user.update_balance(instance.amount, instance.reason)



