from django.db import models

class RiskAssessment(models.Model):
    RISK_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('extreme', 'Extreme'),
    ]

    location = models.ForeignKey('weather.Location', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    risk_level = models.CharField(max_length=10, choices=RISK_LEVELS)
    confidence_score = models.DecimalField(max_digits=4, decimal_places=3)
    factors = models.JSONField()
    recommendations = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.location.name} - {self.risk_level} Risk"

class ExtremeEvent(models.Model):
    EVENT_TYPES = [
        ('flood', 'Flood'),
        ('drought', 'Drought'),
        ('storm', 'Storm'),
        ('heatwave', 'Heat Wave'),
        ('cyclone', 'Cyclone'),
    ]

    SEVERITY_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('extreme', 'Extreme'),
    ]

    location = models.ForeignKey('weather.Location', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    probability = models.DecimalField(max_digits=4, decimal_places=3)
    severity = models.CharField(max_length=10, choices=SEVERITY_LEVELS)
    predicted_start = models.DateTimeField()
    predicted_end = models.DateTimeField()
    description = models.TextField()
    precautions = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['predicted_start']

    def __str__(self):
        return f"{self.event_type} at {self.location.name}"

class WeatherTrend(models.Model):
    TREND_TYPES = [
        ('temperature', 'Temperature'),
        ('precipitation', 'Precipitation'),
        ('wind', 'Wind'),
        ('pressure', 'Pressure'),
    ]

    location = models.ForeignKey('weather.Location', on_delete=models.CASCADE)
    trend_type = models.CharField(max_length=20, choices=TREND_TYPES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    data_points = models.JSONField()
    analysis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.trend_type} Trend - {self.location.name}"

class SafetyRecommendation(models.Model):
    RISK_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('extreme', 'Extreme'),
    ]

    location = models.ForeignKey('weather.Location', on_delete=models.CASCADE)
    weather_condition = models.CharField(max_length=100)
    risk_level = models.CharField(max_length=10, choices=RISK_LEVELS)
    recommendation = models.TextField()
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority', '-created_at']

    def __str__(self):
        return f"{self.weather_condition} - {self.risk_level}" 