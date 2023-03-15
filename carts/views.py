from .models import Cart
from .serializer import CartSerializer
from .mixins import ListCreateAPIView, UpdateDestroyAPIView

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import status
from rest_framework.response import Response

# from users.permissions import IsObjOwner


class CartView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    serializer_class = CartSerializer

    pagination_class = None

    def post(self, request, *args, **kwargs):
        user_id = request.user.id

        serialized = CartSerializer(data=request.data)
        serialized.is_valid()

        serialized.save(user_id=user_id)

        return Response(serialized.data, status.HTTP_201_CREATED)

    def get_queryset(self):
        req_user_id = self.request.user.id

        return [Cart.objects.get(user_id=req_user_id)]


class CartManageView(UpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    serializer_class = CartSerializer
