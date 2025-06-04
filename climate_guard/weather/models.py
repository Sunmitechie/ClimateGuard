from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.country}"

    class Meta:
        unique_together = ['latitude', 'longitude']
        indexes = [
            models.Index(fields=['latitude', 'longitude']),
        ]

class WeatherData(models.Model):
    RISK_LEVELS = [
        ('LOW', 'Green - Low Risk'),
        ('MEDIUM', 'Yellow - Medium Risk'),
        ('HIGH', 'Red - High Risk'),
    ]

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    wind_speed = models.FloatField(validators=[MinValueValidator(0)])
    wind_direction = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(360)]
    )
    precipitation = models.FloatField(validators=[MinValueValidator(0)])
    pressure = models.FloatField(validators=[MinValueValidator(0)])
    weather_description = models.CharField(max_length=255)
    risk_level = models.CharField(max_length=10, choices=RISK_LEVELS)
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['location', 'timestamp']),
            models.Index(fields=['risk_level']),
        ]

class WeatherAlert(models.Model):
    SEVERITY_LEVELS = [
        ('INFO', 'Information'),
        ('WARNING', 'Warning'),
        ('SEVERE', 'Severe'),
        ('EXTREME', 'Extreme'),
    ]

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_LEVELS)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    instructions = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['location', 'start_time', 'end_time']),
            models.Index(fields=['severity']),
            models.Index(fields=['is_active']),
        ]

class UserLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)
    notification_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'location']
        indexes = [
            models.Index(fields=['user', 'is_primary']),
        ]

class WeatherForecast(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    forecast_time = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    wind_speed = models.FloatField(validators=[MinValueValidator(0)])
    wind_direction = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(360)]
    )
    precipitation_probability = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    weather_description = models.CharField(max_length=255)
    risk_level = models.CharField(max_length=10, choices=WeatherData.RISK_LEVELS)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['forecast_time']
        indexes = [
            models.Index(fields=['location', 'forecast_time']),
            models.Index(fields=['risk_level']),
        ]
