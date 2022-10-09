
from django.conf.urls import include, url
from django.contrib import admin
from joins.views import *
from libs.views import *

urlpatterns = [
    url(r'^$', register_view, name='login'),
    url(r'^logout/$', Logout, name='logout'),
    url(r'^password/$', change_password, name='change_password'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^signup-confirmation/$', signup_confirmation, name='signup-confirmation'),
    url(r'^user-img/$', user_img, name='user-img'),

]
