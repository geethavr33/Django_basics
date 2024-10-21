from django.contrib import admin
from .models import Student


class Student_admin(admin.ModelAdmin):
    list_display = ('name', 'roll_no','class_teacher','physics_marks',
                    'chemistry_marks', 'maths_marks', 'total_marks', 'percentage')
admin.site.register(Student, Student_admin)
# Register  your models here.
