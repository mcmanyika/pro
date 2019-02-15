from django.conf.urls import include, url
from django.contrib import admin
from sale.views import *

urlpatterns = [
    url(r'^$', stocks, name='stocks'),

    #url(r'^loggedin/', loggedin, name='loggedin'),
]