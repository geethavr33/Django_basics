from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notification, Messaging
from messaging.models import Messaging
from user.models import User
from user.serializers import UserSerializer
from .serializers import NotificationSerializer, MessagingSerializer

class UnreadNotificationsView(APIView):
    def get(self, request, user_id):
        notifications = Notification.objects.filter(user_id=user_id, status='Unread')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class IncompleteProfileNotificationView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        if not user.profile or not user.preferences:
            notification_message = "Please complete your profile and preferences."
            Notification.objects.create(
                user=user,
                notification_type="Profile Incomplete",
                message=notification_message,
                status="Unread"
            )
            return Response(
                {"message": notification_message},
                status=status.HTTP_200_OK
            )
        return Response(
            {"message": "Profile and Preferences are complete."},
            status=status.HTTP_200_OK
        )

class UnreadMessagesView(APIView):
    def get(self, request, user_id):
        messages = Messaging.objects.filter(receiver_id=user_id, status='Sent')
        serializer = MessagingSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
