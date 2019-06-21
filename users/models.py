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

    def update_balance(self, balance, reason, from_user, to_user=None):
        with transaction.atomic():
            if reason is UserChangeBalance.REPLENISH:
                CustomUser.objects.select_for_update().filter(id=from_user.id).update(
                    balance=F('balance') + balance
                )
            elif reason is UserChangeBalance.WITHDRAWAL:
                CustomUser.objects.select_for_update().filter(id=from_user.id).update(
                    balance=F('balance') - balance
                )
            elif reason is UserChangeBalance.TRANSACTION:
                CustomUser.objects.select_for_update().filter(id=to_user.id).update(
                    balance=F('balance') + balance
                )
                CustomUser.objects.select_for_update().filter(id=from_user.id).update(
                    balance=F('balance') - balance
                )


class UserChangeBalance(models.Model):
    REPLENISH = 1
    WITHDRAWAL = 2
    TRANSACTION = 3

    CHOICES = (
        (REPLENISH, 'Replenish'),
        (WITHDRAWAL, 'Withdrawal'),
        (TRANSACTION, 'Transaction'),
    )

    from_user = models.ForeignKey(
        'CustomUser', related_name='from_user',
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        'CustomUser', related_name='to_user',
        on_delete=models.CASCADE, null=True, blank=True
    )
    reason = models.PositiveSmallIntegerField(choices=CHOICES, default=REPLENISH)
    amount = models.DecimalField('Amount', default=0, max_digits=18, decimal_places=6)
    datetime = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=UserChangeBalance)
def balance_post_save(sender, instance, **kwargs):
    instance.user.update_balance(instance.amount, instance.reason, instance.from_user, instance.to_user)



