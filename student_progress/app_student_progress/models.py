from django.db import models
 
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
   
    def save(self, *args, **kwargs):
        self.total_marks = self.maths_marks + self.chemistry_marks + self.physics_marks
        self.percentage = (self.total_marks / 300) * 100
        super(Student, self).save(*args, **kwargs)
   
    def __str__(self):
        return self.name
 
class Teacher(models.Model):
    name=models.CharField(max_length=50)
    emp_id=models.IntegerField(primary_key=True)
    performance=models.FloatField(default=0)