# Generated by Django 4.0.1 on 2022-01-14 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_notification_date_alter_notification_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='date',
        ),
        migrations.AlterField(
            model_name='notification',
            name='comment',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
