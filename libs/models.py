# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from joins.models import t_acct

# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class t_sermon(models.Model):
    title = models.CharField(max_length=50, default='', null=True, blank=True)
    event = models.CharField(max_length=50, default='', null=True, blank=True)
    venue = models.CharField(max_length=50, default='IOC')
    preacher = models.CharField(max_length=50, default='')
    audio = models.FileField(upload_to=upload_location, null=True, blank=True)
    video = models.FileField(upload_to=upload_location, null=True, blank=True)
    notes = models.TextField()
    date = models.DateField(null=True, blank=True)
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

class t_song(models.Model):
    SongTitle = models.CharField(max_length=50, default='', null=True, blank=True)
    Genre = models.CharField(max_length=50, default='', null=True, blank=True)
    #Date = models.CharField(max_length=50, default='25/12/2022')
    Artist = models.CharField(max_length=50, default='')
    audio = models.FileField(upload_to=upload_location, null=True, blank=True)
    video = models.FileField(upload_to=upload_location, null=True, blank=True)
    notes = models.TextField()
    date = models.DateField(null=True, blank=True)
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.SongTitle

class t_payment(models.Model):
    rootid = models.IntegerField()
    pledgeid = models.IntegerField(default='0')
    currency = models.CharField(max_length=20, default='Bond')
    amount = models.CharField(max_length=10,)
    purpose = models.CharField(max_length=30)
    commitment = models.CharField(max_length=20, default='Cash')
    ref = models.CharField(max_length=20, default='', null=True, blank=True)
    user = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.purpose

class t_stationary(models.Model):
    name = models.CharField(max_length=50, default='')
    img = models.FileField(upload_to=upload_location, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    category = models.CharField(max_length=50, default='')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name



class t_attendance(models.Model):
    rootid = models.ForeignKey(t_acct, on_delete=models.CASCADE)
    zone = models.CharField(max_length=120, default='IOC')
    service = models.CharField(max_length=120, default='')
    user = models.IntegerField()
    
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 'Attendance{}'.format(self.id)    





