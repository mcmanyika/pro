from django.contrib import admin
from .models import *

# Register your models here.
class AssetsModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'serial_no', 'department' ,'zone']
	class Meta:
		model = t_assets
admin.site.register(t_assets, AssetsModelAdmin)

