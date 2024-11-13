from rest_framework import serializers
from .models import Messaging

class MessagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messaging
        fields = '__all__'
