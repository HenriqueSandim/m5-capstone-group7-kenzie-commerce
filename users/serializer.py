from rest_framework import serializers

from .models import UserTypeChoice, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "cpf", "first_name", "last_name", "user_type"]
