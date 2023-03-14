from .models import Order, OrderProducts
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import OrderSerializer, OrderProductsSerializer
from rest_framework import generics

class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_url_kwarg = "pk"

