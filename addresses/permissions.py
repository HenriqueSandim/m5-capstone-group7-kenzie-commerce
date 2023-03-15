from rest_framework import permissions
from .models import Address
from rest_framework.views import View


class IsAddressOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Address):
        return bool(
            request.user.is_authenticated and obj.user_id == request.user.id
            or request.user.is_superuser
        )
