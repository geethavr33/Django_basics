from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['school_id', 'name', 'location','created_on','updated_on']
        






