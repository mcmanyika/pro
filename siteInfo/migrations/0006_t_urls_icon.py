# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-11 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteInfo', '0005_auto_20181211_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_urls',
            name='icon',
            field=models.CharField(default='', max_length=120),
        ),
    ]
