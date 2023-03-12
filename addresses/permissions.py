from rest_framework import permissions
from .models import Address
from rest_framework.views import View

class IsAddressOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Address):
        return request.user.is_authenticated and obj.id == request.user.address_id