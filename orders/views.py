from .models import OrderProducts
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import OrderSerializer, OrderProductsSerializer
from rest_framework import generics


class OrderProductsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = OrderProducts.objects.all()
    serializer_class = OrderProductsSerializer


class OrderProductsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = OrderProducts.objects.all()
    serializer_class = OrderProductsSerializer

    lookup_url_kwarg = "pk"

