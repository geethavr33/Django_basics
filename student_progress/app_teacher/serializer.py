from .models import  Teacher  # Importing the Student and Teacher models to define serializers for them
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