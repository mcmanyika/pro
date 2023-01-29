# Generated by Django 2.1.5 on 2019-01-24 10:02

from django.db import migrations, models
import libs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rootid', models.IntegerField()),
                ('pledgeid', models.IntegerField(default='0')),
                ('currency', models.CharField(default='Bond', max_length=20)),
                ('amount', models.IntegerField()),
                ('purpose', models.CharField(max_length=30)),
                ('commitment', models.CharField(default='Cash', max_length=20)),
                ('ref', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('user', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_sermon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('event', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('venue', models.CharField(default='IOC', max_length=50)),
                ('preacher', models.CharField(default='', max_length=50)),
                ('audio', models.FileField(blank=True, null=True, upload_to=libs.models.upload_location)),
                ('video', models.FileField(blank=True, null=True, upload_to=libs.models.upload_location)),
                ('notes', models.TextField()),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SongTitle', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('Genre', models.CharField(blank=True, default='', max_length=50, null=True)),
                #('Date', models.CharField(default='25/12/2022', max_length=50)),
                ('Artist', models.CharField(default='Apostle T Vutabwashe', max_length=50)),
                ('audio', models.FileField(blank=True, null=True, upload_to=libs.models.upload_location)),
                ('video', models.FileField(blank=True, null=True, upload_to=libs.models.upload_location)),
                ('notes', models.TextField()),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_stationary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('img', models.FileField(blank=True, null=True, upload_to=libs.models.upload_location)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(default='', max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
