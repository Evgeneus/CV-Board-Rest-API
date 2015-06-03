from django.db import models
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible
from extuser.models import ExtUser


@python_2_unicode_compatible
class Skill(models.Model):
    skill_type = models.CharField(verbose_name=_('Skill type'), max_length=255)

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')

    def __str__(self):
        return self.skill_type
