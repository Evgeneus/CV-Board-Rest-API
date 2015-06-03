# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import helpers.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0001_initial'),
        ('skills', '0002_auto_20150603_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillRateLog',
            fields=[
                ('user_id', models.ForeignKey(related_name='skill_rate_log', primary_key=True, verbose_name='ExtUser', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rate', helpers.model_fields.IntegerRangeField(verbose_name="User's rate")),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('skill_id', models.ForeignKey(related_name='skill_rate_log', verbose_name='Skill', to='skills.SkillRate')),
            ],
            options={
                'verbose_name': 'Skill Rate Log',
            },
        ),
        migrations.AlterUniqueTogether(
            name='skillratelog',
            unique_together=set([('user_id', 'skill_id')]),
        ),
    ]
