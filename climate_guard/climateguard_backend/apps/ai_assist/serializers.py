from rest_framework import serializers
from .models import ChatSession, SafetyTip, EmergencyResponse

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = (
            'id', 'user', 'query', 'response',
            'timestamp', 'context', 'feedback'
        )
        read_only_fields = ('user',)

class SafetyTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyTip
        fields = (
            'id', 'weather_condition', 'tip_content',
            'priority_level', 'category'
        )

class EmergencyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyResponse
        fields = (
            'id', 'emergency_type', 'response_steps',
            'priority_level', 'contact_info', 'additional_resources'
        ) 