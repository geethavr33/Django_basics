from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from matches.models import Matching
from profiles.models import Profile
from preferences.models import Preferences
from .serializers import MatchingInputSerializer, MatchingOutputSerializer
from .utils import calculate_match_score


class MatchUsersAPIView(APIView):
    """
    REST API to find matching users based on preferences for all profiles.
    """

    def post(self, request):
        input_serializer = MatchingInputSerializer(data=request.data)
        if input_serializer.is_valid():
            try:
                user_id1 = input_serializer.validated_data['user_ids'][0]  # Primary user
                user_ids = Profile.objects.values_list('user_id', flat=True).exclude(user_id=user_id1)
                
                try:
                    user_preferences = Preferences.objects.get(user_id=user_id1)
                except Preferences.DoesNotExist:
                    return Response(
                        {"error": f"Preferences not found for user {user_id1}."},
                        status=status.HTTP_404_NOT_FOUND
                    )

                matches = []
                for user_id in user_ids:
                    try:
                        user_profile = Profile.objects.get(user_id=user_id)
                        
                        if (user_profile.gender == user_preferences.gender and
                            user_profile.religion == user_preferences.religion and
                            user_profile.caste == user_preferences.caste and
                            # user_profile.profession == user_preferences.profession and
                            # user_profile.height <= user_preferences.height and
                            # user_profile.weight <= user_preferences.weight and
                            user_profile.education == user_preferences.education):
                            
                            match_score = calculate_match_score(user_preferences, user_profile)
                            match = Matching.objects.create(
                                user1_id=user_id1,
                                user2_id=user_id,
                                status='accepted',
                                match_score=match_score
                            )
                            matches.append(match)
                    except Profile.DoesNotExist:
                        continue  # Skip this user if profile not found

                output_serializer = MatchingOutputSerializer(matches, many=True)
                return Response(output_serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
