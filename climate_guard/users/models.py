from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from weather.models import Location

class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    is_phone_verified = models.BooleanField(default=False)
    preferred_language = models.CharField(max_length=10, default='en')
    timezone = models.CharField(max_length=50, default='UTC')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class UserProfile(models.Model):
    NOTIFICATION_FREQUENCY = [
        ('IMMEDIATE', 'Immediate'),
        ('HOURLY', 'Hourly'),
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    organization = models.CharField(max_length=100, blank=True)
    notification_frequency = models.CharField(
        max_length=10,
        choices=NOTIFICATION_FREQUENCY,
        default='IMMEDIATE'
    )
    weather_units = models.CharField(
        max_length=1,
        choices=[('C', 'Celsius'), ('F', 'Fahrenheit')],
        default='C'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SafetyPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='safety_preferences')
    evacuation_point = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='evacuation_points'
    )
    has_vehicle = models.BooleanField(default=False)
    has_emergency_kit = models.BooleanField(default=False)
    medical_conditions = models.TextField(blank=True)
    emergency_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserVerification(models.Model):
    VERIFICATION_TYPES = [
        ('PHONE', 'Phone Number'),
        ('EMAIL', 'Email Address'),
        ('ID', 'Government ID'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verification_type = models.CharField(max_length=5, choices=VERIFICATION_TYPES)
    verification_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['user', 'verification_type']
        indexes = [
            models.Index(fields=['user', 'verification_type']),
            models.Index(fields=['verification_code']),
        ]
