from django.db import models
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible
from extuser.models import ExtUser
from company.models import Job


@python_2_unicode_compatible
class RequestFromUser(models.Model):
    user = models.ForeignKey(ExtUser, verbose_name=_('Request from user'), related_name='request_from_user')
    job = models.ForeignKey(Job, verbose_name=_('Requested job'), related_name='request_from_user')
    added_at = models.DateTimeField(verbose_name='Added at', auto_now_add=True)

    class Meta:
        verbose_name = _('Reauest from user')
        verbose_name_plural = _('Reauests from users')
        unique_together = ('user', 'job')

    def __str__(self):
        return 'request from user:{user}, to job: {job}'\
            .format(user=self.user, job=self.job)


@python_2_unicode_compatible
class RequestFromCompany(models.Model):
    job = models.ForeignKey(Job, verbose_name=_('Requeste for job'), related_name='request_from_company')
    user = models.ForeignKey(ExtUser, verbose_name=_('Request to user'), related_name='request_from_company')
    added_at = models.DateTimeField(verbose_name='Added at', auto_now_add=True)

    class Meta:
        verbose_name = _('Reauest from company')
        verbose_name_plural = _('Reauests from companies')
        unique_together = ('user', 'job')

    def __str__(self):
        return 'request for job:{job}, to user: {user}'\
            .format(job=self.job, user=self.user)
