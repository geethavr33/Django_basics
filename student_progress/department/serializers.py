from rest_framework import serializers  # Import serializers from Django REST Framework
from .models import Department  # Import the Department model from the current app

class DepartmentSerializer(serializers.ModelSerializer):
    # The DepartmentSerializer uses the ModelSerializer base class for serialization
    class Meta:
        # Specify the model to be serialized
        model = Department
        
        # Define the fields to include in the serialized output
        fields = ['dept_id', 'name', 'hod', 'sc_id', 'created_on', 'updated_on']
        # - 'dept_id': The primary key of the department.
        # - 'name': The name of the department.
        # - 'hod': The Head of Department (HOD), referenced as a ForeignKey to the Teacher model.
        # - 'sc_id': The school the department belongs to, referenced as a ForeignKey to the School model.
        # - 'created_on': The timestamp for when the department was created.
        # - 'updated_on': The timestamp for when the department was last updated.
