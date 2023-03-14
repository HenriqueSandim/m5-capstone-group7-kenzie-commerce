from rest_framework import serializers
from .models import Order, OrderProducts

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "order_at", "total_price", "status", "products"]
        depth = 1


class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProducts
        fields = ["id", "quantity", "order", "product"]
        depth = 1

    