# serializers.py
from rest_framework import serializers
from .models import MasterCode

class MasterCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterCode
        fields = '__all__'
