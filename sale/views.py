# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.db import connection
from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from sale.models import *
from siteInfo.models import *
from sale.forms import *

# Create your views here.

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]



def stocks(request):
    leftlinks = t_dictionary.objects.filter(category='leftlinks').order_by('id')
    lftlinks = t_urls.objects.filter(category='leftlinks').order_by('id')

    row = t_product.objects.all().order_by('-id')

    form = SaleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
       
    
    context = {
        "leftlinks" : leftlinks,
        "lftlinks" : lftlinks,
        "form" : form,
        "rows": row,
        }
    template = "stocks.html"
    return render(request, template, context)
