from .models import Cart
from .serializer import CartSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from users.permissions import IsObjOwner


class CartView(CreateAPIView):
    serializer_class = CartSerializer


class CartDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsObjOwner]

    queryset = Cart.objects.all()

    serializer_class = CartSerializer
