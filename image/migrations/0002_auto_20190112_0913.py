# Generated by Django 2.0.1 on 2019-01-12 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rootid', models.IntegerField()),
                ('image', models.ImageField(blank=True, default='', upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Flower',
        ),
    ]
