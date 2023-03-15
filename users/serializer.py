from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, UserTypeChoice

from addresses.serializer import AddressSerializer

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
        match validated_data["user_type"]:
            case "Cliente":
                validated_data["is_staff"] = False
            case "Vendedor":
                validated_data["is_staff"] = True
            case "Administrador":
                validated_data["is_superuser"] = True

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict):

        update_password = validated_data.pop("password")
        if update_password:
            instance.set_password(update_password)

        if validated_data.get("user_type"):
            if validated_data["user_type"] == "Cliente":
                validated_data["is_staff"] = False
            else:
                validated_data["is_staff"] = True

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
