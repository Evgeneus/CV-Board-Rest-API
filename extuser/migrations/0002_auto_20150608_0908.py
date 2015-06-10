# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import helpers.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extuser',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='extuser',
            name='role',
            field=helpers.model_fields.IntegerRangeField(default=0, verbose_name=b'Role'),
        ),
    ]
