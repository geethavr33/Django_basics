from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Subscription
from .serializers import SubscriptionSerializer
from datetime import date

class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures the user is logged in

    def post(self, request):
        subscription_data = request.data.copy()
        subscription_data['user'] = request.user.id  # Bind user to subscription

        serializer = SubscriptionSerializer(data=subscription_data)
        if serializer.is_valid():
        # Save the subscription only once
            serializer.save()
            return Response({
                "message": f"{serializer.data['plan_type']} subscription created for {request.user.username}.",
                "subscription_details": serializer.data,
            }, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        user = request.user
        subscription = Subscription.objects.filter(user=user, status='Active').first()

        if not subscription:
            return Response({"error": "No active subscription found."}, status=status.HTTP_404_NOT_FOUND)

        features = {
            "priority_support": subscription.plan_type == 'Premium',
            "exclusive_content": subscription.plan_type == 'Premium',
            "extended_match_suggestions": subscription.plan_type == 'Premium'
        }

        serializer = SubscriptionSerializer(subscription)
        return Response({
            "message": "Subscription details fetched successfully.",
            "subscription_details": serializer.data,
            "features": features
        }, status=status.HTTP_200_OK)
