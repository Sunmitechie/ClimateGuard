from rest_framework import serializers
from .models import RiskAssessment, ExtremeEvent, WeatherTrend, SafetyRecommendation

class RiskAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskAssessment
        fields = (
            'id', 'location', 'timestamp', 'risk_level',
            'confidence_score', 'factors', 'recommendations'
        )

class ExtremeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtremeEvent
        fields = (
            'id', 'location', 'event_type', 'probability',
            'severity', 'predicted_start', 'predicted_end',
            'description', 'precautions'
        )

class WeatherTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherTrend
        fields = (
            'id', 'location', 'trend_type', 'start_date',
            'end_date', 'data_points', 'analysis'
        )

class SafetyRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyRecommendation
        fields = (
            'id', 'location', 'weather_condition',
            'risk_level', 'recommendation', 'priority'
        ) 