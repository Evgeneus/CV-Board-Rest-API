from django.db import models
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible
from extuser.models import ExtUser
from helpers.model_fields import IntegerRangeField


@python_2_unicode_compatible
class Skill(models.Model):
    skill_type = models.CharField(verbose_name=_('Skill type'), max_length=255)

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')

    def __str__(self):
        return self.skill_type


@python_2_unicode_compatible
class SkillRate(models.Model):
    user_id = models.ForeignKey(ExtUser, verbose_name=_('User'), related_name='skill_rate')
    skill_id = models.ForeignKey(Skill, verbose_name=_('Skill'), related_name='skill_rate')
    self_rate = IntegerRangeField(verbose_name=_('Self rate'), min_value=1, max_value=10, blank=True, null=True)
    guests_rate = IntegerRangeField(verbose_name=_('Guests rate'), min_value=1, max_value=10, blank=True, null=True)
    result_rate = IntegerRangeField(verbose_name=_('Result rate'), min_value=1, max_value=10, blank=True, null=True)

    class Meta:
        verbose_name = _('Skill Rate')
        unique_together = ('user_id', 'skill_id')

    def __str__(self):
        return 'user: {user_id}, skill: {skill_id}'.format(user_id=self.user_id, skill_id=self.skill_id)


@python_2_unicode_compatible
class SkillRateLog(models.Model):
    user_id = models.ForeignKey(ExtUser, primary_key=True, verbose_name=_('ExtUser'), related_name='skill_rate_log')
    skill_id = models.ForeignKey(SkillRate, verbose_name=_('Skill'), related_name='skill_rate_log')
    rate = IntegerRangeField(verbose_name=_("User's rate"), min_value=1, max_value=10)
    date = models.DateTimeField(verbose_name=_('Date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Skill Rate Log')
        unique_together = ('user_id', 'skill_id')

    def __str__(self):
        return 'skill: {skill_id}, rate: {rate}'.format(skill_id=self.skill_id, rate=self.rate)
