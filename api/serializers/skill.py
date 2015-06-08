__all__ = ['SkillRateSerializer']

from rest_framework import serializers


class SkillRateSerializer(serializers.Serializer):
    user_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    skill_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    self_rate = serializers.IntegerField(min_value=0, max_value=10)
    guest_rate = serializers.IntegerField(min_value=0, max_value=10)
    result_rate = serializers.IntegerField(min_value=0, max_value=10)

    def update(self, instance, validated_data):
        instance.self_rate = validated_data.get('self_rate', instance.self_rate)
        instance.save()

        return instance
