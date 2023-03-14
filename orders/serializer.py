from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Order, OrderProducts
from carts.models import Cart

class OrderSerializer(serializers.ModelSerializer):

    def create(self, validated_data: dict) -> Order:
        cart = get_object_or_404(Cart, user_id=validated_data.user_id)

        validated_data["total_price"] = cart["total_price"]
    
        products_list = cart.pop("products")

        for product_dict in products_list:
            validated_data.products.add(product_dict)

        return Order.objects.create(**validated_data)
    

    class Meta:
        model = Order
        fields = ["id", "order_at", "total_price", "status", "products"]
        depth = 1


class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProducts
        fields = ["id", "quantity", "order", "product"]
        depth = 1

    