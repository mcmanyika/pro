# Generated by Django 3.2.22 on 2023-10-13 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0012_auto_20231013_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_acct',
            name='years_in_ministry',
        ),
    ]
