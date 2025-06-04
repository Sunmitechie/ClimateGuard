from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import DashboardSettings

User = get_user_model()

class DashboardOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = fields

class AnalyticsSerializer(serializers.Serializer):
    time_range = serializers.CharField()
    data_points = serializers.ListField()
    summary = serializers.DictField()

class ReportSerializer(serializers.Serializer):
    report_type = serializers.CharField()
    generated_at = serializers.DateTimeField()
    data = serializers.DictField()

class DashboardSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardSettings
        fields = (
            'id', 'user', 'default_view', 'refresh_interval',
            'display_preferences', 'widgets_configuration'
        )
        read_only_fields = ('user',) 