from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Product
from .serializer import ProductSerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = []


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = []

    lookup_url_kwarg = "product_id"
