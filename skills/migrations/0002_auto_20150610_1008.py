# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillrate',
            name='guests_rate',
            field=models.FloatField(null=True, verbose_name='Guests rate', blank=True),
        ),
        migrations.AlterField(
            model_name='skillrate',
            name='result_rate',
            field=models.FloatField(null=True, verbose_name='Result rate', blank=True),
        ),
    ]
