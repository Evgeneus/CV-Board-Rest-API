__all__ = ['SearchUsersSerializer']

from rest_framework import serializers


class SearchUsersSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=40, required=False)
    last_name = serializers.CharField(max_length=40, required=False)
    location = serializers.CharField(max_length=40, required=False)
    role = serializers.IntegerField(min_value=0, max_value=2, required=False)
