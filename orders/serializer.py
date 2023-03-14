from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Order, OrderProducts


class OrderSerializer(serializers.ModelSerializer):

    def create(self, validated_data: dict) -> Order:
        cart = validated_data["user"].cart

        validated_data["total_price"] = cart.total_price
    
        validated_data["products"] = cart.products

        return Order.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        instance.save()

        return instance
    

    class Meta:
        model = Order
        fields = ["id", "order_at", "total_price", "status", "products"]
        depth = 1


class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProducts
        fields = ["id", "quantity", "order", "product"]
        depth = 1

    