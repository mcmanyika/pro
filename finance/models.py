# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class t_dict(models.Model):
    name = models.CharField(max_length=120, default="")
    link = models.CharField(max_length=120, default="")
    category = models.CharField(max_length=120, default="")
    user_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class t_sub(models.Model):
    rootid = models.ForeignKey(t_dict, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=120,
    )
    user_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class t_payment(models.Model):
    rootid = models.IntegerField()
    pledgeid = models.IntegerField(default="0")
    currency = models.CharField(max_length=20, default="Bond")
    amount = models.CharField(
        max_length=10,
    )
    purpose = models.CharField(max_length=30)
    commitment = models.CharField(max_length=20, default="Cash")
    ref = models.CharField(max_length=20, default="", null=True, blank=True)
    user = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.purpose


class t_expense(models.Model):
    payment_from = models.CharField(max_length=50)
    payment_to = models.CharField(max_length=50)
    purpose = models.CharField(
        max_length=10,
    )
    unit = models.IntegerField(default="0")
    unit_cost = models.IntegerField(default="0")
    total_cost = models.IntegerField(default="0")
    notes = models.CharField(max_length=200)
    user = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.purpose
