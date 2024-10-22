from django.db import models

class Student(models.Model):
    roll_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    physics_marks = models.FloatField()
    chemistry_marks = models.FloatField()
    maths_marks = models.FloatField()
    
    teacher_id=models.ForeignKey('Teacher',on_delete=models.DO_NOTHING,null=True,blank=True)
    performance = models.FloatField(default=0.0)
    def __str__(self):
        return f'{self.name} ({self.roll_no})'

    # Calculate performance based on marks
    def calculate_performance(self):
        total_marks = self.physics_marks + self.chemistry_marks + self.maths_marks
        self.performance = total_marks / 3 if total_marks > 0 else 0  # Average performance

    # Overriding save method to calculate performance before saving
    def save(self, *args, **kwargs):
        self.calculate_performance()  # Calculate performance before saving
        super().save(*args, **kwargs)
    @property
    def total_marks(self):
        return self.physics_marks + self.chemistry_marks + self.maths_marks

    @property
    def percentage(self):
        return (self.total_marks / 300) * 100

    def __str__(self):
        return f'{self.name} ({self.roll_no})'
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.name

# Create your models here.
