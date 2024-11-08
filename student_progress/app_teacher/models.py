from django.apps import apps
from django.db import models




# Model to represent a teacher
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.AutoField(primary_key=True)
    performance = models.FloatField(default=0)
    
    # Foreign Key to School
    sc_id = models.ForeignKey('school.School', on_delete=models.DO_NOTHING,null=True,blank=True)
       
    dept_id = models.ManyToManyField('department.Department', related_name='teachers',blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)
 
   

    def save(self, *args, **kwargs):
        # Check if `is_active` status has changed
        if self.pk is not None:  # Ensures this is an update and not a new creation
            old_instance = Teacher.objects.get(pk=self.pk)
            if old_instance.is_active != self.is_active:
                # Lazy-load the Student_Task model to avoid circular import issues
                Student_Task = apps.get_model('app_student_progress', 'Student')
 
                # Update `is_active` status for students related to this teacher
                Student_Task.objects.filter(teacher_id=self).update(is_active=self.is_active)
 
        # Save the teacher instance
        super().save(*args, **kwargs)
 
    
    def __str__(self):
        return self.name

# Create your models here.
