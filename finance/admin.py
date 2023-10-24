# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# Register your models here.
class DictModelAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "timestamp"]

    class Meta:
        model = t_dict


admin.site.register(t_dict, DictModelAdmin)


class SubModelAdmin(admin.ModelAdmin):
    list_display = ["rootid", "name", "timestamp"]

    class Meta:
        model = t_sub


admin.site.register(t_sub, SubModelAdmin)


class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ["rootid", "amount", "purpose", "timestamp"]

    class Meta:
        model = t_payment


admin.site.register(t_payment, PaymentModelAdmin)
