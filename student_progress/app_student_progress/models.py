from django.db import models
from school.models import School  # Import School model
from department.models import Department  # Import Department model
from django.utils import timezone
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField(primary_key=True)
    maths_marks=models.FloatField()
    chemistry_marks=models.FloatField()
    physics_marks=models.FloatField()
    total_marks=models.FloatField(editable=False,null=True,blank=True)
    percentage=models.FloatField(editable=False,null=True,blank=True)
    # classteacher=models.CharField(max_length=50, null=True, blank=True)
    teacher_id = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.total_marks = self.maths_marks + self.chemistry_marks + self.physics_marks
        self.percentage = (self.total_marks / 300) * 100
        super(Student, self).save(*args, **kwargs)
   
    def __str__(self):
        return self.name
 
 # app_student_progress/models.py
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.IntegerField(primary_key=True)
    performance = models.FloatField(default=0)
    
    # Foreign Key to School
    sc_id = models.ForeignKey('school.School', on_delete=models.DO_NOTHING,null=True,blank=True)
    
    # Foreign Key to Department (for normal department association)
    depart_id = models.ForeignKey('department.Department', on_delete=models.DO_NOTHING, null=True, blank=True)
    
    # Foreign Key for HOD designation (distinct from normal department association)
    #hod = models.ForeignKey('app_student_progress.Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='department_hod')


    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
