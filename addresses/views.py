from .models import Address
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import AddressSerializer
from .permissions import IsAddressOwner
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

class AddressView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)

class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAddressOwner]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    lookup_url_kwarg = "pk"

