# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_auto_20150609_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillratelog',
            old_name='skill',
            new_name='skill_rate',
        ),
        migrations.AlterUniqueTogether(
            name='skillratelog',
            unique_together=set([('user', 'skill_rate')]),
        ),
    ]
