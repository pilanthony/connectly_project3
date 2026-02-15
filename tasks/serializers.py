from rest_framework import serializers
from .models import User, Task

#Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at'] # Include all relevant fields

#Serializer for the Task model with validation for assigned_to
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) # String representation of the assigned user for readability

    class Meta:
        model =Task
        fields = ['id', 'title', 'description', 'assigned_to', 'created_at']

        def validate_assigned_to(self,value):  #Custom validation to ensure the assigned user exists
            if not User.objects.filter(id=value.id).exist():
                raise serializers.ValidationError("Assigned user does not exist.")
            return value
