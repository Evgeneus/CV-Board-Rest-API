# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0004_skillrate_result_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillrate',
            old_name='skill_id',
            new_name='skill',
        ),
        migrations.RenameField(
            model_name='skillrate',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='skillratelog',
            old_name='skill_id',
            new_name='skill',
        ),
        migrations.RenameField(
            model_name='skillratelog',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='skillrate',
            unique_together=set([('user', 'skill')]),
        ),
        migrations.AlterUniqueTogether(
            name='skillratelog',
            unique_together=set([('user', 'skill')]),
        ),
    ]
