# Generated by Django 5.1.2 on 2024-10-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
