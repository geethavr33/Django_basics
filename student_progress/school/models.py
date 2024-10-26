from datetime import timezone
from django.db import models
# model for school
class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    school_id = models.AutoField(primary_key=True) # Unique identifier for the school
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

# Create your models here.
