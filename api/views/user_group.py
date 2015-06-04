__all__ = ['UserViewset', 'GroupViewset']

from django.contrib.auth.models import Group
from extuser.models import ExtUser
from api.serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets


class UserViewset(viewsets.ModelViewSet):
    queryset = ExtUser.objects.all()
    serializer_class = UserSerializer


class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
