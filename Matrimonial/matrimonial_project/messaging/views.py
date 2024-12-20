from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from .models import Messaging
from matches.models import Matching  
from rest_framework.permissions import IsAdminUser
from .serializers import MessagingSerializer
from django.db import transaction

class MatchMessageView(APIView):
    def post(self, request):
        if not request.user.is_admin:
            return Response({"error": "Only admins can send messages."}, status=status.HTTP_403_FORBIDDEN)

        match_id = request.data.get('match_id')
        try:
            match = Matching.objects.get(id=match_id, status__iexact='accepted')
            user1 = match.user1
            user2 = match.user2
            message_text = "Congratulations! You have a new match."

            message_data = [
                {"sender": request.user.id, "receiver": user1.id, "message_text": message_text, "status": "Sent"},
                {"sender": request.user.id, "receiver": user2.id, "message_text": message_text, "status": "Sent"}
            ]

            with transaction.atomic():
                for data in message_data:
                    serializer = MessagingSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "Messages sent successfully."}, status=status.HTTP_201_CREATED)

        except Matching.DoesNotExist:
            return Response({"error": "Match not found or not accepted."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserMessagesView(APIView):
    """
    Retrieve all messages for a specific user by ID.
    """
    permission_classes = [IsAdminUser]
    def get(self, request, user_id):
        if not request.user.is_admin:
            return Response({"error": "Only admins can send messages."}, status=status.HTTP_403_FORBIDDEN)

        try:
            messages = Messaging.objects.filter(receiver_id=user_id)
            
            # Update the status of all "Sent" messages to "Read"
            messages.filter(status='Sent').update(status='Read')

            serializer = MessagingSerializer(messages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MatchMessagingView(APIView):
    """
    API view to send messages when a match is detected between two users.
    """

    def post(self, request, *args, **kwargs):
        user1_id = request.data.get('user1_id')
        user2_id = request.data.get('user2_id')

        if not user1_id or not user2_id:
            return Response({"error": "Both user1_id and user2_id are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user1 = User.objects.get(id=user1_id)
            user2 = User.objects.get(id=user2_id)
        except User.DoesNotExist:
            return Response({"error": "One or both users do not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Check if a match exists (you might have a matching model to query)
        match_detected = True  # Replace this with actual match detection logic

        if match_detected:
            message_user1_to_user2 = {
                "sender": user1.id,
                "receiver": user2.id,
                "message_text": "You have a new match with {0}!".format(user2.username),
                "status": "Sent",
            }

            message_user2_to_user1 = {
                "sender": user2.id,
                "receiver": user1.id,
                "message_text": "You have a new match with {0}!".format(user1.username),
                "status": "Sent",
            }

            serializer1 = MessagingSerializer(data=message_user1_to_user2)
            serializer2 = MessagingSerializer(data=message_user2_to_user1)

            if serializer1.is_valid() and serializer2.is_valid():
                serializer1.save()
                serializer2.save()
                return Response(
                    {"message": "Messages sent to both users."}, status=status.HTTP_201_CREATED
                )
            return Response(
                {"errors": {"user1_message": serializer1.errors, "user2_message": serializer2.errors}},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            return Response({"error": "No match detected."}, status=status.HTTP_400_BAD_REQUEST)