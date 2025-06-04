from django.db import models
from django.conf import settings

class ChatSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    query = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    context = models.JSONField(default=dict)
    feedback = models.IntegerField(null=True, blank=True)  # 1-5 rating
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"

class SafetyTip(models.Model):
    PRIORITY_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    CATEGORIES = [
        ('general', 'General'),
        ('storm', 'Storm'),
        ('flood', 'Flood'),
        ('drought', 'Drought'),
        ('heatwave', 'Heat Wave'),
        ('emergency', 'Emergency'),
    ]

    weather_condition = models.CharField(max_length=100)
    tip_content = models.TextField()
    priority_level = models.CharField(max_length=10, choices=PRIORITY_LEVELS)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority_level', '-created_at']

    def __str__(self):
        return f"{self.weather_condition} - {self.category}"

class EmergencyResponse(models.Model):
    PRIORITY_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    emergency_type = models.CharField(max_length=100)
    response_steps = models.JSONField()  # List of steps to follow
    priority_level = models.CharField(max_length=10, choices=PRIORITY_LEVELS)
    contact_info = models.JSONField()  # Emergency contact information
    additional_resources = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority_level']

    def __str__(self):
        return f"{self.emergency_type} Response" 