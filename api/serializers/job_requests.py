__all__ = ['RequestFromUserSerializer']

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from jobrequest.models import RequestFromUser
from company.models import Job


class RequestFromUserSerializer(serializers.Serializer):
    job_id = serializers.IntegerField(min_value=1)

    def create(self, validated_data):
        job_id = validated_data.get('job_id')
        job = get_object_or_404(Job, id=job_id)
        user = validated_data.get('user')

        instance = RequestFromUser.objects.create(user=user, job=job)

        return instance
