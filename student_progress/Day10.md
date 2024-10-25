# Department and School Models Integration
Today, I worked on integrating the Department and School models. Both models have foreign key relationships with the Teacher model.

Tasks:

* Added the Department and School models.
* Linked the Teacher model with both Department and School.
Code Changes:

```python
# models.py
class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

class Department(models.Model):
    name = models.CharField(max_length=100)
    hod = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
```
## API for CRUD Operations in School and Department
* I developed CRUD APIs for the School and Department models, allowing for the creation, reading, updating, and deletion of records.

## Tasks:

* Created serializers for School and Department.
* Implemented viewsets for CRUD operations.
#### Code Changes:

```python
# serializers.py
from rest_framework import serializers
from app_student_progress.models import School, Department

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

# views.py
from rest_framework import viewsets
from app_student_progress.models import School, Department
from app_student_progress.serializers import SchoolSerializer, DepartmentSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
```
