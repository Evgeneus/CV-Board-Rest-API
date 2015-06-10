# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import helpers.model_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_type', models.CharField(max_length=255, verbose_name='Skill type')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='SkillRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('self_rate', helpers.model_fields.IntegerRangeField(null=True, verbose_name='Self rate', blank=True)),
                ('guests_rate', helpers.model_fields.IntegerRangeField(null=True, verbose_name='Guests rate', blank=True)),
                ('result_rate', helpers.model_fields.IntegerRangeField(null=True, verbose_name='Result rate', blank=True)),
                ('skill', models.ForeignKey(related_name='skill_rate', verbose_name='Skill', to='skills.Skill')),
                ('user', models.ForeignKey(related_name='skill_rate', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Skill Rate',
            },
        ),
        migrations.CreateModel(
            name='SkillRateLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', helpers.model_fields.IntegerRangeField(verbose_name="User's rate")),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('skill_rate', models.ForeignKey(related_name='skill_rate_log', verbose_name='Skill', to='skills.SkillRate')),
                ('user', models.ForeignKey(related_name='skill_rate_log', verbose_name='ExtUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Skill Rate Log',
            },
        ),
        migrations.AlterUniqueTogether(
            name='skillratelog',
            unique_together=set([('user', 'skill_rate')]),
        ),
        migrations.AlterUniqueTogether(
            name='skillrate',
            unique_together=set([('user', 'skill')]),
        ),
    ]
