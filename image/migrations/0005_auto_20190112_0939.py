# Generated by Django 2.0.1 on 2019-01-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_auto_20190112_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(blank=True, default='', upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
