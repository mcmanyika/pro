# Generated by Django 3.2.22 on 2023-10-12 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0005_auto_20190112_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]