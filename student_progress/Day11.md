# Assigning HOD to a Department
* I ensured that only one teacher can be the Head of Department (HOD) for a department.

## Tasks:

* Modified the Department model to ensure only one teacher can be assigned as HOD.
* Added validation to prevent multiple teachers from being HODs in the same department.
#### Code Changes:

```python
# models.py(department)
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
# urls.py
from django.urls import path
from .views import DepartmentListCreateView, DepartmentRetrieveUpdateDeleteView

urlpatterns = [
    path('', DepartmentListCreateView.as_view(), name='department-list-create'),  # GET and POST
    path('<int:pk>/', DepartmentRetrieveUpdateDeleteView.as_view(), name='department-detail'),  # GET, PUT, DELETE
]

# models.py(School)
lass School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    school_id = models.AutoField(primary_key=True)  # Unique identifier for the school
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
# urls.py
from django.urls import path
from .views import SchoolListCreateView, SchoolRetrieveUpdateDeleteView

urlpatterns = [
    path('', SchoolListCreateView.as_view(), name='school-list-create'),  # GET and POST
    path('<int:pk>/', SchoolRetrieveUpdateDeleteView.as_view(), name='school-detail'),  # GET, PUT, DELETE
    
]
