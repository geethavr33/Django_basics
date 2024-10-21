from django.db import models



class Student(models.Model):
    roll_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    physics_marks = models.FloatField()
    chemistry_marks = models.FloatField()
    maths_marks = models.FloatField()
    class_teacher = models.CharField(max_length=100)
  

    @property
    def total_marks(self):
        return self.physics_marks + self.chemistry_marks + self.maths_marks

    @property
    def percentage(self):
        return (self.total_marks / 300) * 100

    def __str__(self):
        return f'{self.name} ({self.roll_no})'

# Create your models here.
