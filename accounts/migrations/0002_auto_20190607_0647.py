# Generated by Django 2.0.3 on 2019-06-07 06:47

import accounts.managers
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='useraccount',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('user_objects', accounts.managers.UserAccountManager()),
            ],
        ),
    ]
