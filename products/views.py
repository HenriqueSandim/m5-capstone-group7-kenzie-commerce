from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsAdminOrOwner, IsSellerAdminOrReadOnly, IsAdminOrOwnerOrReadOnly

from .models import Product
from .serializer import ProductSerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "category"]

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerAdminOrReadOnly]

    def post(self, request, *args, **kwargs):
        serialized = ProductSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save(user=request.user)

        return Response(serialized.data, status.HTTP_201_CREATED)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOwnerOrReadOnly]

    lookup_url_kwarg = "product_id"
