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
    REST API to find matching users based on preferences.
    """

    def post(self, request):
        input_serializer = MatchingInputSerializer(data=request.data)
        if input_serializer.is_valid():
            user_id = input_serializer.validated_data['user_id']
            
            try:
                user_preferences = Preferences.objects.get(user_id=user_id)
                user_profile = Profile.objects.get(user_id=user_id)

                # Query the database to find matching users
                matches = Profile.objects.filter(
                    age__range=(int(user_preferences.age.split('-')[0]), int(user_preferences.age.split('-')[1])),
                    religion=user_preferences.religion,
                    caste=user_preferences.caste,
                    education=user_preferences.education,
                    gender=user_preferences.gender,
                    profession=user_preferences.profession,
                    income=user_preferences.income,
                    height__gte=user_preferences.height,
                    weight__gte=user_preferences.weight
                ).exclude(user=user_profile.user)
                
                for match in matches:
                    Matching.objects.create(
                        user1_id=user_profile.user.id,
                        user2_id=match.user.id,
                        status = 'accepted',
                        match_score=calculate_match_score(user_profile, match)  # You can define a matching logic
                    )
                # Serialize the results
                output_serializer = MatchingOutputSerializer(matches, many=True)
                return Response(output_serializer.data, status=status.HTTP_200_OK)

            except Preferences.DoesNotExist:
                return Response({"error": "Preferences not found for user."}, status=status.HTTP_404_NOT_FOUND)
            except Profile.DoesNotExist:
                return Response({"error": "Profile not found for user."}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
