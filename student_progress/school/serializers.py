from rest_framework import serializers  # Import serializers from Django REST Framework for creating serializers
from .models import School  # Import the School model from the current module

# Serializer for the School model, allowing for easy conversion between model instances and JSON
class SchoolSerializer(serializers.ModelSerializer):
    # Meta class to specify the model and fields to be included in the serialization
    class Meta:
        model = School  # Specify the model that this serializer is based on
        fields = ['school_id', 'name', 'location', 'created_on', 'updated_on']  # Define the fields to be serialized
