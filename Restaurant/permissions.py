from rest_framework import permissions

# from django.contrib.auth.models import User


class IsAdminUserReadOnly(permissions.IsAdminUser):
    def has_permissions(request, self, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
