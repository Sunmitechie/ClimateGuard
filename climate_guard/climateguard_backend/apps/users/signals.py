from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile, SafetyPreference

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create UserProfile and SafetyPreference when a new user is created."""
    if created:
        UserProfile.objects.create(user=instance)
        SafetyPreference.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save UserProfile and SafetyPreference when User is saved."""
    if hasattr(instance, 'profile'):
        instance.profile.save()
    if hasattr(instance, 'safety_preferences'):
        instance.safety_preferences.save() 