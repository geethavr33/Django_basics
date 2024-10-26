from .models import Student ,Teacher
from rest_framework import serializers
class Teacher_serializer(serializers.ModelSerializer):
      
    class Meta:
            model = Teacher
            fields = ['emp_id', 'name', 'performance', 'sc_id', 'depart_id', 'created_on', 'updated_on']
    
class Student_serializer(serializers.ModelSerializer):
    #teacher_id = Teacher_serializer(read_only=True)
    total_marks = serializers.ReadOnlyField()
    percentage = serializers.ReadOnlyField()
    class Meta:
            model = Student
            fields=[
                'roll_no','name','physics_marks','chemistry_marks','maths_marks','teacher_id','total_marks','percentage','created_on','updated_on'
                ]
