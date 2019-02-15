# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-07 05:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_auto_20180303_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_sale',
            name='rootid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.t_product'),
        ),
        migrations.AlterField(
            model_name='t_sale',
            name='status',
            field=models.CharField(default='verified', max_length=50),
        ),
    ]
