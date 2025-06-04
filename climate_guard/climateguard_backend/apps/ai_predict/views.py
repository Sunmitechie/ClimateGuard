from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import RiskAssessment, ExtremeEvent, WeatherTrend, SafetyRecommendation
from .serializers import (
    RiskAssessmentSerializer,
    ExtremeEventSerializer,
    WeatherTrendSerializer,
    SafetyRecommendationSerializer
)

class RiskAssessmentView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RiskAssessmentSerializer

    def get_object(self):
        location_id = self.request.query_params.get('location_id')
        return RiskAssessment.objects.filter(location_id=location_id).first()

class ExtremeEventPredictionView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ExtremeEventSerializer

    def get_queryset(self):
        location_id = self.request.query_params.get('location_id')
        return ExtremeEvent.objects.filter(location_id=location_id)

class WeatherTrendView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WeatherTrendSerializer

    def get_queryset(self):
        location_id = self.request.query_params.get('location_id')
        return WeatherTrend.objects.filter(location_id=location_id)

class SafetyRecommendationView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SafetyRecommendationSerializer

    def get_queryset(self):
        location_id = self.request.query_params.get('location_id')
        return SafetyRecommendation.objects.filter(location_id=location_id) 