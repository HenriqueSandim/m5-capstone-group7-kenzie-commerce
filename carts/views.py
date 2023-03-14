from .models import Cart
from .serializer import CartSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.permissions import IsObjOwner


class CartView(ListCreateAPIView):
    serializer_class = CartSerializer

    pagination_class = None

    def get_queryset(self):
        req_user_id = self.request.user.id

        user_cart = Cart.objects.filter(user_id=req_user_id)

        return user_cart


class CartDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsObjOwner]

    queryset = Cart.objects.all()

    serializer_class = CartSerializer
