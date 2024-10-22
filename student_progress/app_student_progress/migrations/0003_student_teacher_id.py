# Generated by Django 5.1.2 on 2024-10-22 05:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_student_progress', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_student_progress.teacher'),
        ),
    ]