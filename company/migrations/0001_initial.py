# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='First name')),
                ('address', models.CharField(max_length=500, verbose_name='Address', blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='Email address')),
                ('location', models.CharField(max_length=40, verbose_name='Location', blank=True)),
                ('type', models.CharField(max_length=256, verbose_name='Company type')),
                ('description', models.TextField(verbose_name='Company description', blank=True)),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Added date')),
                ('last_change', models.DateTimeField(auto_now=True, verbose_name='Last change')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.ForeignKey(related_name='company_manager', verbose_name='Company', to='company.Company')),
                ('manager', models.ForeignKey(related_name='company_manager', verbose_name='Manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Company Manager',
                'verbose_name_plural': 'Companis Managers',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='First name')),
                ('salary', models.FloatField(null=True, verbose_name='Salary', blank=True)),
                ('description', models.TextField(verbose_name='Company description', blank=True)),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Added date')),
                ('last_change', models.DateTimeField(auto_now=True, verbose_name='Last change')),
                ('company', models.ForeignKey(related_name='job', verbose_name='Company', to='company.Company')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.AlterUniqueTogether(
            name='companymanager',
            unique_together=set([('company', 'manager')]),
        ),
    ]
