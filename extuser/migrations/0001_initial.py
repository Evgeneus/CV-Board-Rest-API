# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=40, verbose_name=b'First name')),
                ('last_name', models.CharField(max_length=40, verbose_name=b'Last name')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'Email address')),
                ('date_of_birth', models.DateField(verbose_name=b'Birthday')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is active')),
                ('is_admin', models.BooleanField(default=False, verbose_name=b'Is admin')),
                ('age', models.IntegerField(null=True, verbose_name=b'Age', blank=True)),
                ('desired_salary', models.IntegerField(null=True, verbose_name=b'Desired salary', blank=True)),
                ('register_date', models.DateField(auto_now_add=True, verbose_name=b'Register date')),
                ('last_change', models.DateTimeField(auto_now=True, verbose_name=b'Last change')),
                ('location', models.CharField(max_length=40, verbose_name=b'Location')),
                ('other', models.TextField(verbose_name=b'Other informations', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
