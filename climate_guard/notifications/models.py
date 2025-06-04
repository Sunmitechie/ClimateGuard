from django.db import models
from django.contrib.auth import get_user_model
from weather.models import Location, WeatherAlert

User = get_user_model()

class NotificationPreference(models.Model):
    NOTIFICATION_METHODS = [
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
        ('PUSH', 'Push Notification'),
        ('IN_APP', 'In-App Notification'),
    ]

    SEVERITY_LEVELS = [
        ('ALL', 'All Notifications'),
        ('SEVERE_ONLY', 'Severe and Extreme Only'),
        ('EXTREME_ONLY', 'Extreme Only'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_method = models.CharField(max_length=10, choices=NOTIFICATION_METHODS)
    severity_threshold = models.CharField(max_length=15, choices=SEVERITY_LEVELS, default='ALL')
    is_enabled = models.BooleanField(default=True)
    quiet_hours_start = models.TimeField(null=True, blank=True)
    quiet_hours_end = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'notification_method']

class Notification(models.Model):
    NOTIFICATION_STATUS = [
        ('PENDING', 'Pending'),
        ('SENT', 'Sent'),
        ('FAILED', 'Failed'),
        ('READ', 'Read'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weather_alert = models.ForeignKey(WeatherAlert, on_delete=models.CASCADE)
    notification_preference = models.ForeignKey(NotificationPreference, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=NOTIFICATION_STATUS, default='PENDING')
    sent_at = models.DateTimeField(null=True, blank=True)
    read_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'status']),
            models.Index(fields=['created_at']),
        ]

class NotificationDeliveryLog(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    attempt_number = models.PositiveIntegerField(default=1)
    success = models.BooleanField()
    error_message = models.TextField(null=True, blank=True)
    delivery_method = models.CharField(max_length=10, choices=NotificationPreference.NOTIFICATION_METHODS)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['notification', 'timestamp']),
            models.Index(fields=['success']),
        ]

class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emergency_contacts')
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    relationship = models.CharField(max_length=100)
    notify_on_extreme = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['user', 'notify_on_extreme']),
        ]
