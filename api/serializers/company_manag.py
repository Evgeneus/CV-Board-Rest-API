from company.models import Company, CompanyManager

__all__ = ['CompanySerializer']

from rest_framework import serializers


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=400)
    address = serializers.CharField(max_length=500, required=False)
    email = serializers.EmailField(max_length=255)
    location = serializers.CharField(max_length=40, required=False)
    type = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)

    def create(self, validated_data):
        manager = validated_data.pop('manager')
        company = Company.objects.create(**validated_data)
        CompanyManager.objects.create(company=company, manager=manager)

        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.location = validated_data.get('location', instance.location)
        instance.type = validated_data.get('type', instance.type)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance
