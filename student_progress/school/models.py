from datetime import timezone  # Import timezone for handling time-related functionalities
from django.db import models   # Import models module for creating Django models

class ActiveManager(models.Manager):
    def  get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    
    def active_count(self):
       return self.get_queryset().count()
   
    def get_active(self):
      return self.get_queryset().filter(is_active=True)
   
    def get_inactive(self):
        return self.get_queryset().filter(is_active=False)

# Model for representing a school
class School(models.Model):
    # Field to store the name of the school with a maximum length of 100 characters
    name = models.CharField(max_length=100)

    # Field to store the location of the school with a maximum length of 100 characters
    location = models.CharField(max_length=100)

    # Unique identifier for the school, automatically incremented
    school_id = models.AutoField(primary_key=True)

    # Field to store the creation timestamp, automatically set when a school instance is created
    created_on = models.DateTimeField(auto_now_add=True)

    # Field to store the last updated timestamp, automatically set when a school instance is updated
    updated_on = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
 
    objects = models.Manager()  # The default manager
    active_objects = ActiveManager()

    # String representation of the School model, returns the name of the school
    def __str__(self):
        return self.name

# Create your models here.
