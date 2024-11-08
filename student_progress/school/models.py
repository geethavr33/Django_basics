from datetime import timezone  # Import timezone for handling time-related functionalities
from django.db import models   # Import models module for creating Django models
from django.apps import apps  # Import apps module for accessing Django apps

# Model for representing a school
class School(models.Model):
    # Field to store the name of the school with a maximum length of 100 characters
    name = models.CharField(max_length=100)

    # Field to store the location of the school with a maximum length of 100 characters
    location = models.CharField(max_length=100)

    # Unique identifier for the school, automatically incremented
    sc_id = models.AutoField(primary_key=True)
    depart_id =models.ManyToManyField('department.Department',blank=True)
    #depart_id = models.ForeignKey('department.Department', on_delete=models.CASCADE, related_name='school_departments', null=True)

    # Field to store the creation timestamp, automatically set when a school instance is created
    created_on = models.DateTimeField(auto_now_add=True)

    # Field to store the last updated timestamp, automatically set when a school instance is updated
    updated_on = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
 
    
    
    def save(self, *args, **kwargs):
        # Track if the `is_active` field changes
        if self.pk is not None:  # Only check if the instance already exists
            old_instance = School.objects.get(pk=self.pk)
            if old_instance.is_active != self.is_active:
                # Lazy-load related models to avoid circular import issues
                Teachers = apps.get_model('teacher', 'Teacher')
                Student = apps.get_model('student', 'Student')
 
                # Update the `is_active` status of teachers in this school
                Teachers.objects.filter(sc_id=self).update(is_active=self.is_active)
 
                # Update the `is_active` status of students associated with teachers in this school
                Student.objects.filter(teacher_id__sc_id=self).update(is_active=self.is_active)
 
        # Call the parent class's save method to save the instance
        super(School, self).save(*args, **kwargs)
    # String representation of the School model, returns the name of the school
    def __str__(self):
        return self.name

# Create your models here.
