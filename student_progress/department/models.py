from django.db import models
from django.forms import ValidationError

# from School import models as school_model
# from app_student_progress import models as Teacher_model
# Create your models here.
# from app_student_progress.models import Teacher
 

class Department(models.Model):
    name=models.CharField(max_length=100)
    hod = models.ForeignKey('app_student_progress.Teacher',on_delete=models.DO_NOTHING,null=True,blank=True)
    dept_id=models.IntegerField(primary_key=True)
    sc_id = models.ForeignKey('school.School', on_delete=models.DO_NOTHING,null=True,blank=True)
    

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Check if another department has the same HOD
        if self.hod and Department.objects.filter(hod=self.hod).exclude(department_id=self.department_id).exists():
            raise ValidationError(f'{self.hod} is already assigned as the HOD of another department.')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
