from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Cart:
        return Cart.objects.create(**validated_data)

    class Meta:
        model = Cart
        fields = [
            "id",
            "total_price",
            "user_id",
        ]

        read_only_fields = ["id", "user_id"]
