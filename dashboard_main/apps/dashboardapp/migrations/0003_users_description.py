# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0002_users_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='description',
            field=models.TextField(default='hello!'),
            preserve_default=False,
        ),
    ]
