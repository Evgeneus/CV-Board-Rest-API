__all__ = ['IsUserOrAdmin']

from rest_framework import permissions
from helpers import roles


class IsUserOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role in (roles.ROLE_ADMIN, roles.ROLE_USER):
            return True
        return False
