# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# Register your models here.
class SermonModelAdmin(admin.ModelAdmin):
    list_display = ["title", "date"]

    class Meta:
        model = t_sermon


admin.site.register(t_sermon, SermonModelAdmin)


class StationaryModelAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "timestamp"]

    class Meta:
        model = t_stationary


admin.site.register(t_stationary, StationaryModelAdmin)


class AttendanceModelAdmin(admin.ModelAdmin):
    list_display = ["rootid", "service", "zone", "timestamp"]

    class Meta:
        model = t_attendance


admin.site.register(t_attendance, AttendanceModelAdmin)
