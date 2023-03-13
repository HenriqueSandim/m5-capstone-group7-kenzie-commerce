from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_superuser
            or obj == request.user
        )
    

class IsObjOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_superuser
            or obj.owner == request.user
        )


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_staff
            or request.user.is_superuser
        )
