from django.contrib import admin
from .models import Student,Teacher,School,Department


class Student_admin(admin.ModelAdmin):
    list_display = ('name', 'roll_no','teacher_id','physics_marks',
                    'chemistry_marks', 'maths_marks', 'total_marks', 'percentage')
admin.site.register(Student, Student_admin)
admin.site.register(Teacher)
admin.site.register(School)
admin.site.register(Department)
# Register  your models here.
