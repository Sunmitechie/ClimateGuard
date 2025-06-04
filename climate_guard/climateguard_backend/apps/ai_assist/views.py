from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import ChatSession, SafetyTip, EmergencyResponse
from .serializers import (
    ChatSessionSerializer,
    SafetyTipSerializer,
    EmergencyResponseSerializer
)

class ChatView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChatSessionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SafetyTipsView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SafetyTipSerializer

    def get_queryset(self):
        weather_condition = self.request.query_params.get('weather_condition')
        return SafetyTip.objects.filter(weather_condition=weather_condition)

class EmergencyResponseView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EmergencyResponseSerializer

    def get_object(self):
        emergency_type = self.request.query_params.get('emergency_type')
        return EmergencyResponse.objects.filter(emergency_type=emergency_type).first() 