# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-04 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteInfo', '0008_auto_20181222_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_dictionary',
            name='user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
