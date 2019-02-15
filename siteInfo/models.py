from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class t_urls(models.Model):
    name = models.CharField(max_length=120, default='')
    link = models.CharField(max_length=120, default='')
    category = models.CharField(max_length=120, default='')
    icon = models.CharField(max_length=120, default='')
    status = models.CharField(max_length=20, default='Active')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name

class t_sub_url(models.Model):
    rootid = models.ForeignKey(t_urls, on_delete=models.CASCADE,)
    name = models.CharField(max_length=120, default='')
    link = models.CharField(max_length=120, default='')
    category = models.CharField(max_length=120, default='')
    icon = models.CharField(max_length=120, default='')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name

class t_dictionary(models.Model):
    name = models.CharField(max_length=120, default='')
    link = models.CharField(max_length=120, default='')
    category = models.CharField(max_length=120, default='')
    sub_category = models.CharField(max_length=20, default='')
    user = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name

