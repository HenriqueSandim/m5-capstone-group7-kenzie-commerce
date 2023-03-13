from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.hashers import make_password

from .models import User, UserTypeChoice

from utils.custom_errors import choices_error_message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                    "id", "username", "email", "cpf", "password",
                    "first_name", "last_name", "user_type", "is_staff",
                    "is_superuser", "is_active", "date_joined", "last_login"
                ]
        extra_kwargs = {
            "password": {
                "write_only": True
            },
            "cpf": {
                "validators": {
                    UniqueValidator(queryset=User.objects.all()),
                }
            },
            "user_type": {
                "required": True,
                "error_messages": {
                    "invalid_choice": choices_error_message(UserTypeChoice)
                }
            }
        }

    def create(self, validated_data):
        if validated_data["user_type"] == "Cliente":
            validated_data["is_staff"] = False
        else:
            validated_data["is_staff"] = True

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict):
        if validated_data.get("password"):
            instance.set_password(validated_data["password"])

        if validated_data.get("user_type"):
            if validated_data["user_type"] == "Cliente":
                validated_data["is_staff"] = False
            else:
                validated_data["is_staff"] = True

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
