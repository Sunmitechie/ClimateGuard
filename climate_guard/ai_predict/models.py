from django.db import models
from weather.models import Location, WeatherData
import numpy as np
from django.conf import settings
import tensorflow as tf
import joblib
from pathlib import Path
from django.core.validators import MinValueValidator, MaxValueValidator

class WeatherPredictionModel(models.Model):
    MODEL_TYPES = [
        ('TEMPERATURE', 'Temperature Prediction'),
        ('PRECIPITATION', 'Precipitation Prediction'),
        ('RISK', 'Risk Assessment'),
    ]

    name = models.CharField(max_length=255)
    model_type = models.CharField(max_length=20, choices=MODEL_TYPES)
    version = models.CharField(max_length=50)
    model_file = models.FileField(upload_to='ai_models/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['name', 'version']

    def load_model(self):
        model_path = Path(settings.MEDIA_ROOT) / self.model_file.name
        if self.model_type == 'RISK':
            return joblib.load(model_path)
        return tf.keras.models.load_model(model_path)

class RiskAssessmentResult(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    weather_data = models.ForeignKey(WeatherData, on_delete=models.CASCADE)
    model = models.ForeignKey(WeatherPredictionModel, on_delete=models.CASCADE)
    risk_score = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(1)]
    )
    risk_factors = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['location', 'created_at']),
            models.Index(fields=['risk_score']),
        ]

    @property
    def risk_level(self):
        if self.risk_score < settings.RISK_THRESHOLD_LOW:
            return 'LOW'
        elif self.risk_score < settings.RISK_THRESHOLD_MEDIUM:
            return 'MEDIUM'
        return 'HIGH'

class ModelPerformanceMetric(models.Model):
    model = models.ForeignKey(WeatherPredictionModel, on_delete=models.CASCADE)
    accuracy = models.FloatField()
    precision = models.FloatField()
    recall = models.FloatField()
    f1_score = models.FloatField()
    mae = models.FloatField()  # Mean Absolute Error
    rmse = models.FloatField()  # Root Mean Square Error
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['model', 'timestamp']),
        ]
