# Generated by Django 5.1.2 on 2024-10-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_student_progress', '0003_student_teacher_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='employee_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
