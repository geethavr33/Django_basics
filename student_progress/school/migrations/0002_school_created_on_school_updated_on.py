# Generated by Django 5.1.2 on 2024-10-24 05:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
