from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404,  redirect
from django.db import connection
from django.db.models import Q
from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import FormView
from .models import *
from siteInfo.forms import TitleForm

# Create your views here.


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def title(request):
    title = t_dictionary.objects.filter(category='title')
    instance = get_object_or_404(t_dictionary, category='title')
    form = TitleForm(request.POST or None,
                     request.FILES or None, instance=instance)

    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")

    context = {
        "form": form,
        "name": instance.name,

    }
    template = "site_settings.html"
    return render(request, template, context)
