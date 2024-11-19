from rest_framework import serializers
from matches.models import Matching


class MatchingInputSerializer(serializers.Serializer):
    user_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    )
class MatchingOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matching
        fields = ['user1_id', 'user2_id', 'match_score', 'status', 'created_on']  # Include actual fields here
