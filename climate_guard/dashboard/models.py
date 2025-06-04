from django.db import models
from django.contrib.auth import get_user_model
from weather.models import Location, WeatherData
from ai_predict.models import RiskAssessmentResult

User = get_user_model()

class DashboardPreference(models.Model):
    CHART_TYPES = [
        ('LINE', 'Line Chart'),
        ('BAR', 'Bar Chart'),
        ('RADAR', 'Radar Chart'),
        ('HEAT', 'Heat Map'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    preferred_chart_type = models.CharField(max_length=5, choices=CHART_TYPES, default='LINE')
    show_risk_indicators = models.BooleanField(default=True)
    show_historical_data = models.BooleanField(default=True)
    data_refresh_interval = models.IntegerField(default=300)  # in seconds
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class WeatherAnalytics(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    average_temperature = models.FloatField()
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    average_humidity = models.FloatField()
    total_precipitation = models.FloatField()
    average_wind_speed = models.FloatField()
    dominant_wind_direction = models.FloatField()
    risk_level_distribution = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['location', 'date']
        indexes = [
            models.Index(fields=['location', 'date']),
        ]

class RiskTrend(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    risk_trend_data = models.JSONField()
    trend_direction = models.CharField(
        max_length=10,
        choices=[
            ('INCREASING', 'Increasing Risk'),
            ('STABLE', 'Stable Risk'),
            ('DECREASING', 'Decreasing Risk'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['location', 'start_date', 'end_date']),
            models.Index(fields=['trend_direction']),
        ]

class UserInteractionLog(models.Model):
    INTERACTION_TYPES = [
        ('VIEW', 'View Dashboard'),
        ('FILTER', 'Apply Filter'),
        ('EXPORT', 'Export Data'),
        ('SHARE', 'Share Dashboard'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_TYPES)
    interaction_details = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'interaction_type']),
            models.Index(fields=['timestamp']),
        ]

class SavedDashboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    configuration = models.JSONField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'name']
        indexes = [
            models.Index(fields=['user', 'is_public']),
        ]
