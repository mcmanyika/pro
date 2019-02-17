# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from libs.models import t_payment

# Register your models here.
class DictModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'category','timestamp']
	class Meta:
		model = t_dict
admin.site.register(t_dict, DictModelAdmin)

class SubModelAdmin(admin.ModelAdmin):
	list_display = ['rootid','name','timestamp']
	class Meta:
		model = t_sub
admin.site.register(t_sub, SubModelAdmin)

