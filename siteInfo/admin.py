from django.contrib import admin
from .models import *


# Register your models here.

class UrlsModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'category','timestamp']
	class Meta:
		model = t_urls
admin.site.register(t_urls, UrlsModelAdmin)

class SubUrlsModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'category','timestamp']
	class Meta:
		model = t_sub_url
admin.site.register(t_sub_url, SubUrlsModelAdmin)

class DictModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'category','timestamp']
	class Meta:
		model = t_dictionary
admin.site.register(t_dictionary, DictModelAdmin)
