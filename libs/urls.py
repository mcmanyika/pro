from django.conf.urls import include, url
from django.contrib import admin
from joins.views import *
from libs.views import *

urlpatterns = [
   url(r'^children/', children, name='children'),
   url(r'^users/', users, name='users'),

    url(r'^user-details/(?P<id>.*)$', user_details, name='user-details'),
    url(r'^user-confirmation/', user_confirmation, name='user-confirmation'),
	url(r'^attendance/', attendance, name='attendance'),
]