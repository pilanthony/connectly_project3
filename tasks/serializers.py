from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


# =========================
# USER SERIALIZER (with password hashing)
# =========================
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )


# =========================
# TASK SERIALIZER
# =========================
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'created_at']

    def validate_assigned_to(self, value):
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Assigned user does not exist.")
        return value
