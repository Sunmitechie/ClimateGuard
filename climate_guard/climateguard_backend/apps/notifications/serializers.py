from rest_framework import serializers
from .models import Notification, NotificationSettings

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'id', 'user', 'title', 'message',
            'notification_type', 'is_read', 'created_at',
            'priority', 'action_url'
        )
        read_only_fields = ('user', 'created_at')

class NotificationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSettings
        fields = (
            'id', 'user', 'email_notifications',
            'push_notifications', 'sms_notifications',
            'notification_frequency', 'quiet_hours_start',
            'quiet_hours_end', 'emergency_override'
        )
        read_only_fields = ('user',) 