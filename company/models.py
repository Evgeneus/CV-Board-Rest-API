from django.db import models
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible
from extuser.models import ExtUser


@python_2_unicode_compatible
class Company(models.Model):
    name = models.CharField(verbose_name=_('Company'), max_length=40)
    address = models.CharField(verbose_name=_('Address'), max_length=500, blank=True)
    email = models.EmailField(verbose_name=_('Email address'), max_length=255, unique=True)
    location = models.CharField(verbose_name=_('Location'), max_length=40, blank=True)
    type = models.CharField(verbose_name=_('Company type'), max_length=256)
    description = models.TextField(verbose_name=_('Company description'), blank=True)
    added_at = models.DateTimeField(verbose_name=_('Added date'), auto_now_add=True)
    last_change = models.DateTimeField(verbose_name=_('Last change'), auto_now=True)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return 'company: {name}'.format(name=self.name)


@python_2_unicode_compatible
class CompanyManager(models.Model):
    company = models.ForeignKey(Company, verbose_name=_('Company'), related_name='company_manager')
    manager = models.ForeignKey(ExtUser, verbose_name=_('Manager'), related_name='company_manager')

    class Meta:
        verbose_name = _('Company Manager')
        verbose_name_plural = _('Companis Managers')
        unique_together = ('company', 'manager')

    def __str__(self):
        return 'company: {company}, manager: {manager}'.format(company=self.company, manager=self.manager)


@python_2_unicode_compatible
class Job(models.Model):
    name = models.CharField(verbose_name=_('Job'), max_length=40)
    description = models.TextField(verbose_name=_('Company description'), blank=True)
    salary = models.FloatField(verbose_name=_('Salary'), blank=True, null=True)
    added_at = models.DateTimeField(verbose_name=_('Added date'), auto_now_add=True)
    last_change = models.DateTimeField(verbose_name=_('Last change'), auto_now=True)
    company = models.ForeignKey(Company, verbose_name=_('Company'), related_name='job')

    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')

    def __str__(self):
        return 'job: {name}'.format(name=self.name)
