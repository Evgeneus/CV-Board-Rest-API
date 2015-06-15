__all__ = ['JobSerializer']

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from company.models import Job, Company


class JobSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    description = serializers.CharField(required=False)
    salary = serializers.FloatField(min_value=0, required=False)

    def create(self, validated_data):
        company_id = validated_data.pop('company_id')
        company = get_object_or_404(Company, id=company_id)
        job = Job.objects.create(company=company, **validated_data)

        return job

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.salary = validated_data.get('salary',  instance.salary)
        instance.company = validated_data.get('company', instance.company)
        instance.save()

        return instance
