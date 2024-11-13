from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Messaging, Matching
from .serializers import MessagingSerializer
from django.db import transaction

class MatchMessageView(APIView):
    def post(self, request):
        match_id = request.data.get('match_id')
        print(match_id)

        try:
            # Fetch the accepted match
            
            match = Matching.objects.get(id=match_id, status__iexact='accepted')

            #match = Matching.objects.get(id=match_id, status='Accepted')
            print(match)

            user1 = match.user1
            user2 = match.user2
            print(user1)
            message_text = "Congratulations! You have a new match."

            # Create messages using the serializer
            message_data = [
                {"sender": user1.id, "receiver": user2.id, "message_text": message_text, "status": "Sent"},
                {"sender": user2.id, "receiver": user1.id, "message_text": message_text, "status": "Sent"}
            ]

            with transaction.atomic():
                for data in message_data:
                    serializer = MessagingSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)  # Log the errors for debugging

                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "Messages sent successfully."}, status=status.HTTP_201_CREATED)

        except Matching.DoesNotExist:
            return Response({"error": "Match not found or not accepted."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
