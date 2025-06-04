from rest_framework import serializers
from .models import WeatherData, Location, WeatherAlert

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'user', 'name', 'latitude', 'longitude', 'country', 'city', 'is_default')
        read_only_fields = ('user',)

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = (
            'id', 'location', 'timestamp', 'temperature', 'humidity',
            'wind_speed', 'wind_direction', 'precipitation',
            'pressure', 'data_type', 'description'
        )

class WeatherAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherAlert
        fields = (
            'id', 'location', 'alert_type', 'severity',
            'title', 'description', 'issued_at',
            'expires_at', 'is_active'
        ) 