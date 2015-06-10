__all__ = ['SkillRateLogSerializer']

from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework import serializers

from skills.models import SkillRate, SkillRateLog


class SkillRateLogSerializer(serializers.Serializer):
    skill_rate_id = serializers.IntegerField(min_value=1)
    rate = serializers.IntegerField(min_value=0, max_value=10)

    def create(self, validated_data):
        rate = validated_data.get('rate')
        skill_rate_id = validated_data.get('skill_rate_id')
        user = validated_data.get('user')
        skill_rate = get_object_or_404(SkillRate, id=skill_rate_id)

        if user.id == skill_rate.user_id:
            raise PermissionDenied

        instance = SkillRateLog.objects.create(user=user, skill_rate=skill_rate, rate=rate)

        count_equivalent_entries = SkillRateLog.objects.filter(skill_rate=skill_rate, rate=rate).count()
        self_rate = skill_rate.self_rate
        current_guests_rate = skill_rate.guests_rate

        if current_guests_rate:
                avg_guests_rate = self._avg_guests_rate(skill_rate_id=skill_rate_id)
                SkillRate.objects.filter(id=skill_rate_id).update(guests_rate=avg_guests_rate)

                self._update_result_rate(skill_rate_id=skill_rate_id,
                                         avg_guests_rate=avg_guests_rate, self_rate=self_rate)
        elif count_equivalent_entries == 2:
            self_rate = skill_rate.self_rate

            SkillRate.objects.filter(id=skill_rate_id).update(guests_rate=rate)
            self._update_result_rate(skill_rate_id=skill_rate_id, avg_guests_rate=rate, self_rate=self_rate)

        return instance

    def _avg_guests_rate(self, skill_rate_id):
        rate_list = SkillRateLog.objects.filter(skill_rate=skill_rate_id).values_list('rate')
        sum = 0.
        for rate in rate_list:
            sum += rate[0]
        avg_guests_rate = sum/len(rate_list)

        return avg_guests_rate

    def _update_result_rate(self, skill_rate_id, avg_guests_rate, self_rate):
        result_rate = avg_guests_rate*0.6 + self_rate*0.4

        SkillRate.objects.filter(id=skill_rate_id).update(result_rate=result_rate)
