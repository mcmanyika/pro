
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
from assets.models import *
from siteInfo.views import *
from assets.forms import *

# Create your views here.


def assets(request):

    row = t_assets.objects.all().order_by('-id')

    paginator = Paginator(row, 13)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "row": queryset,
        "page_request_var": page_request_var,
    }
    template = "assets.html"
    return render(request, template, context)


def asset_detail(request, id):
    dictionary = t_dictionary.objects.all().order_by('id')
    instan = get_object_or_404(t_assets, id=id)

    form = NewAssetForm(request.POST or None,
                        request.FILES or None, instance=instan)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/confirmation/')

    context = {
        "rootid": instan.rootid,
        "name": instan.name,
        "serial_no": instan.serial_no,
        "equip_type": instan.equip_type,
        "department": instan.department,
        "zone": instan.zone,
        "user": instan.user,
        "dict": dictionary,

    }
    template = "asset_detail.html"
    return render(request, template, context)


def upload_asset(request):
    dictionary = t_dictionary.objects.all().order_by('id')
    form = NewAssetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/confirmation/')

    context = {
        "form": form,
        "dict": dictionary,

    }
    template = "upload_asset.html"
    return render(request, template, context)
