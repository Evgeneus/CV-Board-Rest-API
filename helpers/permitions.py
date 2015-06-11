__all__ = ['IsUserOrAdmin', 'IsManagerOrAdmin', 'IsManagerOrAdminOrReadOnly']

from rest_framework import permissions
from helpers import roles

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsUserOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role in (roles.ROLE_ADMIN, roles.ROLE_USER):
            return True
        return False


class IsManagerOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role in (roles.ROLE_ADMIN, roles.ROLE_MANAGER):
            return True
        return False


class IsManagerOrAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if ((request.method in SAFE_METHODS) or
                (request.user and request.user.is_authenticated()
                 and request.user.role in (roles.ROLE_ADMIN, roles.ROLE_MANAGER))):
            return True
        return False