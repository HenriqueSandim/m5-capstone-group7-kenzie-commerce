from .models import Order, OrderProducts
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import OrderSerializer, OrderProductsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsObjOwner

from .models import OrderProducts
from .serializer import OrderSerializer, OrderProductsSerializer

class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsObjOwner]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_url_kwarg = "pk"

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)
