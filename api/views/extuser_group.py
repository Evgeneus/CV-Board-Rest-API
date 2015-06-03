__all__ = ['ExtUserViewset', 'GroupViewset']

from django.contrib.auth.models import Group
from extuser.models import ExtUser
from api.serializers import ExtUserSerializer, GroupSerializer
from rest_framework import viewsets


class ExtUserViewset(viewsets.ModelViewSet):
    queryset = ExtUser.objects.all()
    serializer_class = ExtUserSerializer


class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
