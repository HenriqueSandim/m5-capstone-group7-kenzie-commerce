from rest_framework import serializers

from users.models import User
from users.serializer import UserSerializer

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username" ,read_only=True)
    class Meta:
        model = Product
        fields = ["id", "name", "category", "price", "description", "inventory", "user"]
        extra_kwargs = {
            "inventory": {
                "min_value": 1
            }
        }
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
