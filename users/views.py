from rest_framework import generics

from .models import User
from .serializer import UserSerializer
from .permissions import IsAdminOrOwner

from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class UsersViews(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserManageViews(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"
