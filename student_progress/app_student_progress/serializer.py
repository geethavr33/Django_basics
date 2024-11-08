from django.shortcuts import get_object_or_404
from .models import Student  # Importing the Student and Teacher models to define serializers for them
from rest_framework import serializers  # Importing serializers from Django REST Framework for serialization
from app_teacher.models import Teacher

# Serializer for the Student model
class Student_serializer(serializers.ModelSerializer):
    # Defining read-only fields for total_marks and percentage
    total_marks = serializers.ReadOnlyField()  # Total marks will be calculated in the Student model's save method
    percentage = serializers.ReadOnlyField()    # Percentage will also be calculated in the Student model's save method

    class Meta:
        model = Student  # Specify the model that this serializer is associated with
        fields = [  # List of fields to include in the serialized representation
            'roll_no',            # Roll number of the student (primary key)
            'name',               # Name of the student
            #'physics_marks',      # Marks obtained in Physics
            #'chemistry_marks',    # Marks obtained in Chemistry
            #'maths_marks',        # Marks obtained in Mathematics
            'teacher_id',         # Foreign key to the Teacher model
            'sc_id',
            'dept_id',
            'total_marks',        # Total marks (read-only)
            'percentage',         # Percentage (read-only)

            'is_active',  # Boolean indicating if the teacher is active or not
            'created_on',         # Timestamp of when the student record was created
            'updated_on'          # Timestamp of when the student record was last updated
        ]


    def validate_teacher_id(self, value):
        # Extract relevant IDs from data
        teacher_id = self.initial_data.get('teacher_id')
        school_id = self.initial_data.get('sc_id')
 
        # If a teacher is provided, check department and school consistency
        if teacher_id:
            teacher = get_object_or_404(Teacher, emp_id=teacher_id)
 
 
            if school_id and teacher.sc_id.sc_id != school_id:
                raise serializers.ValidationError(
                    f"Teacher {teacher.emp_id} does not belong to school ID: {school_id}."
                )
           
 
 
            valid_departments = set(teacher.dept_id.values_list('dept_id', flat=True))  # Use .values_list to get IDs
 
            # Check if the provided department ID is valid for the teacher
            department_id = self.initial_data.get('dept_id')
 
            # Check if department_id is in the list of valid departments
            if department_id is not None and department_id not in valid_departments:
                raise serializers.ValidationError(
                    f"Teacher {teacher.emp_id} does not belong to department ID: {department_id}."
                )
        return value
 