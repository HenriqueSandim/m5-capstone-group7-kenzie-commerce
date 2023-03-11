from .models import Cart
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import CartSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView


class CartView(CreateAPIView):
    serializer_class = CartSerializer


class CartDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Cart.objects.all()

    serializer_class = CartSerializer
