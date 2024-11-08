from school.models import School
from .models import  Teacher  # Importing the Student and Teacher models to define serializers for them
from rest_framework import serializers  # Importing serializers from Django REST Framework for serialization
from django.shortcuts import get_object_or_404  # Importing get_object_or_404 to handle 404 errors
# Serializer for the Teacher model
class Teacher_serializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher  # Specify the model that this serializer is associated with
        fields = '__all__'  # Define the fields to be serialized



    def validate_department_ID(self, value):
        # Get the school ID from the input data
        sc_id = self.initial_data.get('sc_id')
       
        if sc_id:
            # Use get_object_or_404 to retrieve the school
            school = get_object_or_404(School, sc_id=sc_id)
           
            # Get the valid department IDs for this school
            valid_departments = set(school.depart_id.values_list('depart_id', flat=True))
 
            # Check if the selected departments are valid for the school
            for department in value:
                if department.dept_id not in valid_departments:
                    raise serializers.ValidationError(
                        f"Department {department.name} (ID: {department.pk}) is not associated with the selected school."
                    )
       
        return value
