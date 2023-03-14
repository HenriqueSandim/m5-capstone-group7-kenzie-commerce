from rest_framework import serializers
from .models import Order, OrderProducts
from django.core.mail import send_mail
from django.conf import settings

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

        send_mail(
            subject = 'Status do seu pedido de compra',
            message = f'Seu pedido foi atualizado pelo vendedor, o status do pedido é {validated_data["status"]}',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [f'{validated_data["user"].email}'],
            fail_silently = False
        )

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

    