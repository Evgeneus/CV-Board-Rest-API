from django.contrib import admin
from skills.models import Skill, SkillRate, SkillRateLog


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_type']


@admin.register(SkillRate)
class SkillRateAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'skill_id', 'self_rate', 'guests_rate', 'result_rate']


@admin.register(SkillRateLog)
class SkillRateLogAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'skill_id', 'rate', 'date']
