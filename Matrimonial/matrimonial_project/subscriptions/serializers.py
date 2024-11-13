from rest_framework import serializers
from .models import Subscription
from datetime import date, timedelta


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
       model = Subscription
       fields = ['id','user', 'plan_type', 'start_date', 'end_date', 'status']
       read_only_fields = [ 'id','start_date', 'end_date', 'status']
    
    def validate_plan_type(self, value):
        if value not in ['Free', 'Premium']:
            raise serializers.ValidationError("Invalid plan type.")
        return value
    def create(self, validated_data):
    # Ensure start_date defaults to today
        validated_data['start_date'] = validated_data.get('start_date', date.today())
    
    # Calculate end_date based on the start_date
        validated_data['end_date'] = validated_data['start_date'] + timedelta(days=90)
    
    # Call the base implementation to create the Subscription
        return super().create(validated_data)
