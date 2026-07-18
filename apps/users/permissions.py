from rest_framework.permissions import BasePermission


class IsAdminGroup(BasePermission):
    message = "Hanya Admin yang dapat mengakses endpoint ini."

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        return request.user.groups.filter(name="Admin").exists()