from .models import Student 
from rest_framework import serializers

class Student_serializer(serializers.ModelSerializer):
    total_marks = serializers.ReadOnlyField()
    percentage = serializers.ReadOnlyField()
    
    class Meta:
        model = Student
        fields=[
            'roll_no','name','physics_marks','chemistry_marks','maths_marks','class_teacher','total_marks','percentage'
            ]
        