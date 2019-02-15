# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class t_product(models.Model):
    name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=50, default='')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name

class t_sale(models.Model):
    rootid = models.ForeignKey(t_product, on_delete=models.CASCADE,)
    price = models.IntegerField()
    qty = models.IntegerField()
    status = models.CharField(max_length=50, default='verified')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.status  