from rest_framework import serializers
from profiles.models import Profile
class MatchingInputSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

class MatchingOutputSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    age = serializers.IntegerField()
    height = serializers.FloatField()
    weight = serializers.FloatField()
    religion = serializers.CharField(source='religion.display_text', read_only=True)
    profession = serializers.CharField(source='profession.display_text', read_only=True)

    class Meta:
        model = Profile
        fields = ['user_id', 'username', 'age', 'height', 'weight', 'religion', 'profession']
