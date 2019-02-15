# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'category']
	class Meta:
		model = t_product
admin.site.register(t_product, ProductModelAdmin)

class SaleModelAdmin(admin.ModelAdmin):
	list_display = ['rootid', 'status']
	class Meta:
		model = t_sale
admin.site.register(t_sale, SaleModelAdmin)