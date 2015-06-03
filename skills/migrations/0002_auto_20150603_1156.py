# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import helpers.model_fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('self_rate', helpers.model_fields.IntegerRangeField(null=True, verbose_name='Self rate', blank=True)),
                ('guests_rate', helpers.model_fields.IntegerRangeField(null=True, verbose_name='Guests rate', blank=True)),
                ('skill_id', models.ForeignKey(related_name='skill_rate', verbose_name='Skill', to='skills.Skill')),
                ('user_id', models.ForeignKey(related_name='skill_rate', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Skill Rate',
            },
        ),
        migrations.AlterUniqueTogether(
            name='skillrate',
            unique_together=set([('user_id', 'skill_id')]),
        ),
    ]
