from rest_framework import serializers  # Import serializers from Django REST Framework
from .models import Department  # Import the Department model from the current app

class DepartmentSerializer(serializers.ModelSerializer):
    # The DepartmentSerializer uses the ModelSerializer base class for serialization
    class Meta:
        # Specify the model to be serialized
        model = Department
        
        # Define the fields to include in the serialized output
        fields = '__all__'
        