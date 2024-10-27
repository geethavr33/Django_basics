from django.db import models
from school.models import School  # Import School model
from department.models import Department  # Import Department model
from django.utils import timezone

# Model to represent a teacher
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.AutoField(primary_key=True)
    performance = models.FloatField(default=0)
    
    # Foreign Key to School
    sc_id = models.ForeignKey('school.School', on_delete=models.DO_NOTHING,null=True,blank=True)
    
    # Foreign Key to Department (for normal department association)
    depart_id = models.ForeignKey('department.Department', on_delete=models.DO_NOTHING, null=True, blank=True)
    #depart_id = models.IntegerField(null=True, blank=True)

    # Timestamps for tracking record creation and updates
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # String representation for easy identification in admin interface
    def __str__(self):
        return self.name

# Create your models here.