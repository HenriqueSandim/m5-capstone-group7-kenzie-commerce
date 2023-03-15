from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Cart, Cart_products


class CartSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Cart:
        return Cart.objects.create(**validated_data)

    class Meta:
        model = Cart
        fields = [
            "id",
            "total_price",
            "user_id",
            "products"
        ]
        extra_kwargs = {
            "id": {
                "read_only": True
            },
            "total_price": {
                "read_only": True
            },
            "user_id": {
                "read_only": True,
                "validators": [
                    UniqueValidator(
                        queryset=Cart.objects.all(),
                        message="User already have an cart"
                    ),
                ]
            }
        }
        depth = 1


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_products
        fields = ["id", "quantity", "cart", "product"]
        read_only_fields = ["id"]
        depth = 1

    def create(self, validated_data):
        return Cart_products.objects.create(**validated_data)
