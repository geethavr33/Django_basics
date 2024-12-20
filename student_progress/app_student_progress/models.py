from django.db import models
from school.models import School  # Import School model
from department.models import Department  # Import Department model
from app_teacher.models import Teacher # Import Teacher model
from django.utils import timezone


class Student(models.Model):
    # Fields for the Student model
    name=models.CharField(max_length=50)
    roll_no=models.AutoField(primary_key=True)
    #maths_marks=models.FloatField()
    #chemistry_marks=models.FloatField()
    #physics_marks=models.FloatField()
    total_marks=models.FloatField(editable=False,null=True,blank=True)
    percentage=models.FloatField(editable=False,null=True,blank=True)
    # Foreign key to the Teacher model; represents the teacher assigned to the student
    teacher_id = models.ForeignKey('app_teacher.Teacher', on_delete=models.DO_NOTHING, null=True, blank=True)
        # Timestamps for tracking record creation and updates
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    sc_id = models.ForeignKey('school.School', on_delete=models.DO_NOTHING,null=True,blank=True)
    dept_id = models.ForeignKey('department.Department', on_delete=models.DO_NOTHING, null=True, blank=True)  # example



        # Override the save method to calculate total marks and percentage before saving
    def save(self, *args, **kwargs):
        self.total_marks = self.maths_marks + self.chemistry_marks + self.physics_marks
        self.percentage = (self.total_marks / 300) * 100

        if self.teacher_id:
            try:
                teacher = Teacher.objects.get(emp_id=self.teacher_id.emp_id)
 
                # Set department if not provided; retrieve the first related department if multiple
                if not self.dept_id:
                    self.dept_id = teacher.dept_id.all().first()
               
                # Set school if not provided
                if not self.sc_id:
                    self.sc_id = teacher.sc_id
            except Teacher.DoesNotExist:
                raise ValueError("The specified teacher does not exist.")
           
 
        super(Student, self).save(*args, **kwargs)


     # String representation for easy identification in admin interface
    def __str__(self):
        return self.name
 