# Generated by Django 5.1.2 on 2024-10-26 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('performance', models.FloatField(default=0)),
                ('depart_id', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('sc_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('roll_no', models.AutoField(primary_key=True, serialize=False)),
                ('maths_marks', models.FloatField()),
                ('chemistry_marks', models.FloatField()),
                ('physics_marks', models.FloatField()),
                ('total_marks', models.FloatField(blank=True, editable=False, null=True)),
                ('percentage', models.FloatField(blank=True, editable=False, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('teacher_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_student_progress.teacher')),
            ],
        ),
    ]
