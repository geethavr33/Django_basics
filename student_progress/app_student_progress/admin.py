from django.contrib import admin  # Importing Django's admin module to manage models in the admin interface
from .models import Student, Teacher, School, Department  # Importing the models to be registered in the admin interface


# Admin configuration for the Student model
class Student_admin(admin.ModelAdmin):
    # Fields to be displayed in the admin list view for the Student model
    list_display = (
        'name',           # Display the student's name
        'roll_no',       # Display the student's roll number
        'teacher_id',    # Display the assigned teacher for the student
        #'physics_marks', # Display marks obtained in Physics
        #'chemistry_marks', # Display marks obtained in Chemistry
        #'maths_marks',   # Display marks obtained in Mathematics
        'total_marks',   # Display the total marks calculated
        'percentage'     # Display the percentage calculated
    )

# Registering the Student model with the custom admin configuration
admin.site.register(Student, Student_admin)

# Registering the Teacher, School, and Department models with the default admin configuration
admin.site.register(Teacher)     # Register Teacher model in the admin interface
admin.site.register(School)      # Register School model in the admin interface
admin.site.register(Department)  # Register Department model in the admin interface

# All models have been registered, making them manageable through the Django admin interface.
