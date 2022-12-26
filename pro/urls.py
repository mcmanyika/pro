"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from libs.views import *
from sale.views import *
from joins.views import *
from finance.views import *
from events.views import calendar
from siteInfo.views import *
from shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart', include('cart.urls')),
    path('orders/', include('orders.urls')),
    url(r'^home/', allmembers, name='home'),
    url(r'^sermons/', sermons, name='sermons'),
    url(r'^sermon/(?P<id>.*)$', sermon, name='sermon'),
    url(r'^edit-sermon/(?P<id>.*)$', edit_sermon, name='edit-sermon'),
    url(r'^hymnals/', hymnals, name='hymnals'),
    url(r'^hymnal/(?P<id>.*)$', hymnal, name='hymnal'),
    url(r'^edit-hymnal/(?P<id>.*)$', edit_hymnal, name='edit-hymnal'),
    url(r'^members/(?P<department>.*)$', members, name='members'),
    url(r'^member-detail/(?P<id>.*)$', member_details, name='member-detail'),
    url(r'^member-payments/(?P<id>.*)$', member_payments, name='member-payments'),
    url(r'^pledge/(?P<id>.*)$', pledge, name='pledge'),
    url(r'^calendar/', calendar_2, name='calendar'),
    url(r'^allmembers/', allmembers, name='allmembers'),
    url(r'^upload-sermon/', upload_sermon, name='upload-sermon'),
    url(r'^upload-hymnal/', upload_hymnal, name='upload-hymnal'),
    url(r'^confirmation/', confirmation, name='confirmation'),
    url(r'^add_member/', add_member, name='add_member'),
    url(r'^stationary/', stationary, name='stationary'),
    url(r'^save/$', ajax_currency,name='save'),
    url(r'^save_member/$', ajax_add_member,name='save_member'),
    url(r'^ajax-add-member/$', ajax_add_member,name='ajax-add-member'),
    url(r'^ajax-search/', ajax_search, name='ajax-search'),
    url(r'^save-child/$', children,name='save-child'),

    

    url(r'^', include('joins.urls')),
    url(r'^login/', include('joins.urls')),
    url(r'^libs/', include('libs.urls')),
    url(r'^assets/', include('assets.urls')),
    url(r'^stocks/', include('sale.urls')),
    url(r'^finance/', include('finance.urls')),
    url(r'^siteInfo/', include('siteInfo.urls')),
    url(r'^site-title/', title, name='site-title'),
    url(r'^csv/', export_data, name='csv'),
    # url(r'^attendance/', attendance, name='attendance'),

    url(r'^add-group/', ajax_group, name='add-group'),
    path('shop/', include('shop.urls')),
    

] 