# Generated by Django 4.0.1 on 2022-01-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/default.jpg', null=True, upload_to='uploads/profile_pictures'),
        ),
    ]