from .models import Address
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import AddressSerializer
from .permissions import IsAddressOwnerOrAdmin
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User


class AddressView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAddressOwnerOrAdmin]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    lookup_url_kwarg = "address_id"
