
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsObjOwner

from .models import OrderProducts
from .serializer import OrderSerializer, OrderProductsSerializer


class OrderProductsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = OrderProducts.objects.all()
    serializer_class = OrderProductsSerializer


class OrderProductsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsObjOwner]

    queryset = OrderProducts.objects.all()
    serializer_class = OrderProductsSerializer

    lookup_url_kwarg = "order_id"
