# Generated by Django 2.2.2 on 2019-07-11 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_transaction_to_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='datetime',
            new_name='created_time',
        ),
    ]
