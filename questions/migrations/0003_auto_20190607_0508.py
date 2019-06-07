# Generated by Django 2.0.3 on 2019-06-07 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_question_asked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='is_answered',
            field=models.BooleanField(default=False),
        ),
    ]
