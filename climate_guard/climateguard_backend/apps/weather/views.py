from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import WeatherData, Location, WeatherAlert
from .serializers import (
    WeatherDataSerializer,
    LocationSerializer,
    WeatherAlertSerializer
)

class WeatherForecastView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WeatherDataSerializer

    def get_queryset(self):
        location_id = self.request.query_params.get('location_id')
        return WeatherData.objects.filter(location_id=location_id, data_type='forecast')

class CurrentWeatherView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WeatherDataSerializer

    def get_object(self):
        location_id = self.request.query_params.get('location_id')
        return WeatherData.objects.filter(
            location_id=location_id,
            data_type='current'
        ).first()

class WeatherAlertView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WeatherAlertSerializer

    def get_queryset(self):
        location_id = self.request.query_params.get('location_id')
        return WeatherAlert.objects.filter(location_id=location_id)

class LocationView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HistoricalWeatherView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WeatherDataSerializer

    def get_queryset(self):
        location_id = self.request.query_params.get('location_id')
        return WeatherData.objects.filter(
            location_id=location_id,
            data_type='historical'
        ).order_by('-timestamp') 