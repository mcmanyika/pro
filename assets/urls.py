from django.conf.urls import include, url
from django.contrib import admin
from assets.views import *

urlpatterns = [
   url(r'^assets/', assets, name='assets'),
   url(r'^upload-asset/', upload_asset, name='upload-asset'),
   url(r'^asset-detail/(?P<id>.*)$', asset_detail, name='asset-detail'),
]