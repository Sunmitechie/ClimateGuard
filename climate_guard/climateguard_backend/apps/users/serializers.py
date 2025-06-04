from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile, SafetyPreference

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'phone_number', 'address', 'city', 'country', 'emergency_contact')
        read_only_fields = ('user',)

class SafetyPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyPreference
        fields = ('id', 'user', 'notification_frequency', 'alert_threshold', 'preferred_contact_method')
        read_only_fields = ('user',)

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        # Add password validation logic here if needed
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value 