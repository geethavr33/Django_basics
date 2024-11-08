from django.db import models
from django.forms import ValidationError
# from School import models as school_model
# from app_student_progress import models as Teacher_model
# Created Department model .
# from app_student_progress.models import Teacher
 

class Department(models.Model):
    # Name of the department, maximum length is 100 character
    name=models.CharField(max_length=100)
    # Foreign key relationship with the Teacher model to indicate the Head of Department (HOD)
    # On deletion, do nothing if the referenced teacher is deleted

    hod = models.ForeignKey('app_teacher.Teacher',on_delete=models.DO_NOTHING,null=True,blank=True)
    # Auto-incrementing primary key for the department
    dept_id=models.AutoField(primary_key=True)
   
    # Timestamp for when the department is created, automatically set to the current time
    created_on = models.DateTimeField(auto_now_add=True)
    
    # Timestamp for when the department is last updated, automatically updated to the current time
   
    updated_on = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
 
    
    def __str__(self):
        # Return the name of the department when the object is represented as a string

        return self.name


