from rest_framework import serializers
from .models import Notification, Messaging

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'notification_type', 'message', 'status', 'created_on', 'updated_on']

class MessagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messaging
        fields = ['id', 'sender', 'receiver', 'message_text', 'status', 'created_on', 'updated_on']
