__all__ = ['SkillRateSerializer']

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from skills.models import SkillRate, Skill


class SkillRateSerializer(serializers.Serializer):
    skill_id = serializers.IntegerField(min_value=1)
    self_rate = serializers.IntegerField(min_value=0, max_value=10)

    def update(self, instance, validated_data):
        instance.self_rate = validated_data.get('self_rate', instance.self_rate)
        instance.save()

        return instance

    def create(self, validated_data):
        skill_id = validated_data.get('skill_id')
        self_rate = validated_data.get('self_rate')
        user = validated_data.get('user')
        skill = get_object_or_404(Skill, pk=skill_id)

        instance = SkillRate.objects.create(user_id=user, skill_id=skill, self_rate=self_rate)

        return instance