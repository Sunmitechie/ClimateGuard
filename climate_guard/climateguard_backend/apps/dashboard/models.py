from django.db import models
from django.conf import settings

class DashboardSettings(models.Model):
    VIEW_CHOICES = [
        ('overview', 'Overview'),
        ('detailed', 'Detailed'),
        ('compact', 'Compact'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    default_view = models.CharField(max_length=20, choices=VIEW_CHOICES, default='overview')
    refresh_interval = models.IntegerField(default=300)  # in seconds
    display_preferences = models.JSONField(default=dict)  # User's display preferences
    widgets_configuration = models.JSONField(default=dict)  # Widget layout and settings
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Dashboard Settings"

    class Meta:
        verbose_name_plural = "Dashboard Settings" 