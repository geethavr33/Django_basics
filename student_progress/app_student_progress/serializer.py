from .models import Student, Teacher  # Importing the Student and Teacher models to define serializers for them
from rest_framework import serializers  # Importing serializers from Django REST Framework for serialization

# Serializer for the Teacher model
class Teacher_serializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher  # Specify the model that this serializer is associated with
        fields = [  # List of fields to include in the serialized representation
            'emp_id',    # Employee ID of the teacher (primary key)
            'name',      # Name of the teacher
            'performance', # Performance metric of the teacher
            'sc_id',     # Foreign key to the School model
            'depart_id', # Foreign key to the Department model
            'created_on', # Timestamp of when the teacher record was created
            'updated_on'  # Timestamp of when the teacher record was last updated
        ]

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
            'physics_marks',      # Marks obtained in Physics
            'chemistry_marks',    # Marks obtained in Chemistry
            'maths_marks',        # Marks obtained in Mathematics
            'teacher_id',         # Foreign key to the Teacher model
            'total_marks',        # Total marks (read-only)
            'percentage',         # Percentage (read-only)
            'created_on',         # Timestamp of when the student record was created
            'updated_on'          # Timestamp of when the student record was last updated
        ]
