# Generated by Django 5.1 on 2024-09-03 08:02

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=account.models.profile_picture_directory_path, verbose_name='Profile Picture'),
        ),
    ]
