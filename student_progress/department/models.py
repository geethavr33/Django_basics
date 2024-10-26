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

    hod = models.ForeignKey('app_student_progress.Teacher',on_delete=models.DO_NOTHING,null=True,blank=True)
    # Auto-incrementing primary key for the department
    dept_id=models.AutoField(primary_key=True)
    # Foreign key relationship with the School model to indicate which school the department belongs to
    # On deletion, do nothing if the referenced school is deleted

    sc_id = models.ForeignKey('school.School', on_delete=models.DO_NOTHING,null=True,blank=True)
    
    # Timestamp for when the department is created, automatically set to the current time
    created_on = models.DateTimeField(auto_now_add=True)
    
    # Timestamp for when the department is last updated, automatically updated to the current time
   
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Check if another department has the same HOD
        # Raise a validation error if the HOD is already assigned to another department

        if self.hod and Department.objects.filter(hod=self.hod).exclude(dept_id=self.dept_id).exists():
            raise ValidationError(f'{self.hod} is already assigned as the HOD of another department.')
        
        # Call the superclass's save method to perform the actual saving of the model instance

        super().save(*args, **kwargs)

    def __str__(self):
        # Return the name of the department when the object is represented as a string

        return self.name
