# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0005_bot_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
