# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import helpers.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20150603_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillrate',
            name='result_rate',
            field=helpers.model_fields.IntegerRangeField(null=True, verbose_name='Result rate', blank=True),
        ),
    ]
