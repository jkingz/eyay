# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 05:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0008_knowledge_is_accepted'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='knowledge',
            unique_together=set([('bot', 'statement')]),
        ),
    ]