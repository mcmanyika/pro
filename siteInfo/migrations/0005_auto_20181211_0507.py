# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-11 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteInfo', '0004_t_sub_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_sub_url',
            name='icon',
            field=models.CharField(default='', max_length=120),
        ),
    ]
