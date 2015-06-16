# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Job'),
        ),
    ]
