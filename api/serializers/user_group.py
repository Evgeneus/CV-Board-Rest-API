__all__ = ['UserSerializer', 'GroupSerializer']

from django.contrib.auth.models import Group
from extuser.models import ExtUser
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtUser
        fields = ('first_name', 'last_name', 'email',
                  'date_of_birth', 'age', 'location',
                  'desired_salary', 'register_date',
                  'last_change', 'is_admin', 'is_active', 'other',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name',)
