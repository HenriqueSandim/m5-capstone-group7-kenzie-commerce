from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    def update(self, instance: Address, validated_data: dict) -> Address:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(validated_data["password"])

        instance.save()

        return instance


    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "number",
            "complement",
            "postal_code",
            "neighborhood",
            "city",
            "state"
        ]