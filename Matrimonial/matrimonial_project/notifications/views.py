from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from messaging.models import Messaging
from user.models import User
from .serializers import NotificationSerializer, MessagingSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied



class IncompleteProfileNotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        if not request.user.is_admin:
            raise PermissionDenied("Only admins can send notifications.")

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


class UnreadMessagesNotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        if not request.user.is_admin:
            raise PermissionDenied("Only admins can send notifications.")

        unread_messages = Messaging.objects.filter(receiver_id=user_id, status='Sent').order_by('-created_on')
        unread_count = unread_messages.count()

        if unread_count > 0:
            notification_message = f"You have {unread_count} unread messages."
            Notification.objects.create(
                user_id=user_id,
                notification_type="Unread Messages",
                message=notification_message,
                status="Unread"
            )
        else:
            notification_message = "No unread messages."

        serializer = MessagingSerializer(unread_messages, many=True)
        return Response(
            {
                "unread_messages": serializer.data,
                "notification": notification_message
            },
            status=status.HTTP_200_OK
        )

class BulkFestivalNotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not request.user.is_admin:
            raise PermissionDenied("Only admins can send bulk notifications.")

        festival_name = request.data.get('festival_name')
        message_template = request.data.get('message', f"Wishing you a joyous {festival_name}!")
        user_ids = request.data.get('user_ids', [])  # List of user IDs to notify

        if not user_ids:
            return Response({"error": "No user IDs provided."}, status=status.HTTP_400_BAD_REQUEST)

        notifications = []
        for user_id in user_ids:
            notifications.append(Notification(
                user_id=user_id,
                notification_type="Festival Greeting",
                message=message_template,
                status="Unread",
                #category=festival_name
            ))

        Notification.objects.bulk_create(notifications)

        return Response({"message": f"Festival notifications sent to {len(user_ids)} users."}, status=status.HTTP_201_CREATED)

class UnreadNotificationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        if not request.user.is_admin:
            raise PermissionDenied("Only admins can view this data.")
        
        notifications = Notification.objects.filter(user_id=user_id, status='Unread').order_by('-created_on')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserNotificationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        # Ensure only the user or admin can access notifications
        if request.user.id != user_id and not request.user.is_admin:
            return Response({"error": "You do not have permission to view these notifications."}, status=status.HTTP_403_FORBIDDEN)

        # Fetch all notifications for the given user_id
        notifications = Notification.objects.filter(user_id=user_id)

        # Update unread notifications to read
        unread_notifications = notifications.filter(status='Unread')
        unread_notifications.update(status='Read')

        # Serialize and return all notifications
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)