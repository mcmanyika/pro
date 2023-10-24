# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from joins.models import t_acct


# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class t_sermon(models.Model):
    title = models.CharField(max_length=50, default="", null=True, blank=True)
    event = models.CharField(max_length=50, default="", null=True, blank=True)
    venue = models.CharField(max_length=50, default="IOC")
    preacher = models.CharField(max_length=50, default="")
    audio = models.FileField(upload_to=upload_location, null=True, blank=True)
    video = models.FileField(upload_to=upload_location, null=True, blank=True)
    notes = models.TextField()
    date = models.DateField(null=True, blank=True)
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title


class t_stationary(models.Model):
    name = models.CharField(max_length=50, default="")
    img = models.FileField(upload_to=upload_location, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    category = models.CharField(max_length=50, default="")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class t_attendance(models.Model):
    rootid = models.ForeignKey(t_acct, on_delete=models.CASCADE)
    zone = models.CharField(max_length=120, default="IOC")
    service = models.CharField(max_length=120, default="")
    user = models.IntegerField()

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "Attendance{}".format(self.id)
