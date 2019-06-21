# Generated by Django 2.2.2 on 2019-06-20 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190616_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserChangeBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.PositiveSmallIntegerField(choices=[(1, 'Replenish'), (2, 'Withdrawal'), (3, 'payment for work')], default=1)),
                ('amount', models.DecimalField(decimal_places=6, default=0, max_digits=18, verbose_name='Amount')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balance_changes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]