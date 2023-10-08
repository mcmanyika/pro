# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
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
from .mixins import AjaxFormMixin
from django.db import models
from joins.models import *
from joins.forms import *
from siteInfo.models import *
from siteInfo.views import *
from libs.forms import *
from libs.views import *
from finance.models import *


# Create your views here.
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


@login_required(login_url="/login/")
def index(request):
    leftlinks = t_dict.objects.filter(category="leftlinks").order_by("id")
    lftlinks = t_urls.objects.filter(category="leftlinks").order_by("id")
    a = t_user_attribute.objects.all()

    row = t_sermon.objects.all().order_by("-id")

    paginator = Paginator(row, 13)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get("page")
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "leftlinks": leftlinks,
        "lftlinks": lftlinks,
        "a": a,
        "row": queryset,
        "page_request_var": page_request_var,
    }
    template = "index.html"
    return render(request, template, context)


@login_required(login_url="/login/")
def sermons(request):
    leftlinks = t_dict.objects.filter(category="leftlinks").order_by("id")
    lftlinks = t_urls.objects.filter(category="leftlinks").order_by("id")
    a = t_user_attribute.objects.all()

    row = t_sermon.objects.all().order_by("-id")

    paginator = Paginator(row, 13)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get("page")
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "leftlinks": leftlinks,
        "lftlinks": lftlinks,
        "a": a,
        "row": queryset,
        "page_request_var": page_request_var,
    }
    template = "sermons.html"
    return render(request, template, context)


def sermon(request, id):
    leftlinks = t_dict.objects.filter(category="leftlinks").order_by("id")
    instance = get_object_or_404(t_sermon, id=id)

    form = SermonForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect("/confirmation/")

    context = {
        "leftlinks": leftlinks,
        "title": instance.title,
        "event": instance.event,
        "venue": instance.venue,
        "preacher": instance.preacher,
        "notes": instance.notes,
    }
    template = "sermon.html"
    return render(request, template, context)


def edit_sermon(request, id):
    leftlinks = t_dict.objects.filter(category="leftlinks").order_by("id")
    instance = get_object_or_404(t_sermon, id=id)
    d = t_dictionary.objects.all()

    form = SermonForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect("/confirmation/")

    context = {
        "leftlinks": leftlinks,
        "form": form,
        "title": instance.title,
        "event": instance.event,
        "venue": instance.venue,
        "preacher": instance.preacher,
        "notes": instance.notes,
        "d": d,
    }
    template = "edit_sermon.html"
    return render(request, template, context)


def members(request, department):
    leftlinks = t_dict.objects.filter(category="leftlinks").order_by("id")
    lftlinks = t_urls.objects.filter(category="leftlinks").order_by("id")
    a = t_user_attribute.objects.filter(department=department)
    row = t_acct.objects.filter(department=department).order_by("-id")
    headings = t_dictionary.objects.all().order_by("id")
    user_p = get_object_or_404(UserProfile, rootid=request.user.id)

    c = connection.cursor()
    c.cursor.execute(
        """Select a.gender, count(a.id) as total
                            FROM joins_t_acct a
                            GROUP BY a.gender
                            """
    )

    c = dictfetchall(c)

    totalFemale = c[0]["total"] if c else 0
    totalMen = c[1]["total"] if c else 0
    totalCount = totalFemale + totalMen

    hlinks = connection.cursor()
    hlinks.cursor.execute(
        """Select u.id, u.icon, u.name as Hname, u.link, u.status
                            FROM siteInfo_t_urls u
                            WHERE u.status = "Active" 
                            ORDER BY -u.id
                            """
    )

    hlinks = dictfetchall(hlinks)

    queryset_list = t_acct.objects.filter().order_by("-id")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(fname__icontains=query) | Q(lname__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get("page")
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "user_p": user_p,
        "totalCount": totalCount,
        "totalFemale": totalFemale,
        "totalMen": totalMen,
        "headings": headings,
        "hlinks": hlinks,
        "leftlinks": leftlinks,
        "lftlinks": lftlinks,
        "a": a,
        "members": queryset,
        "page_request_var": page_request_var,
    }
    template = "members.html"
    return render(request, template, context)


def pledge(request, id):
    pay = get_object_or_404(t_payment, id=id)

    c = connection.cursor()
    c.cursor.execute(
        """Select d.name
                            FROM finance_t_dict d
                            WHERE d.category = 'currency'
                            """
    )

    c = dictfetchall(c)

    pledge = connection.cursor()
    pledge.cursor.execute(
        """Select
                            p.id, p.currency, p.amount, p.purpose, p.timestamp, sum(p.amount) as total
                            FROM libs_t_payment p
                            Where p.pledgeid = %s
                            GROUP BY p.amount, p.purpose, p.timestamp """,
        [id],
    )

    pledge = dictfetchall(pledge)

    acct = connection.cursor()
    acct.cursor.execute(
        """Select
                            a.fname, a.lname, p.pledgeid
                            FROM libs_t_payment p
                            INNER JOIN joins_t_acct a ON a.id = p.rootid
                            Where p.pledgeid = %s""",
        [id],
    )

    acct = dictfetchall(acct)
    fname = acct[0]["fname"] if acct else ""
    lname = acct[0]["lname"] if acct else ""

    pledgeTotal = connection.cursor()
    pledgeTotal.cursor.execute(
        """Select
                            sum(p.amount) as total
                            FROM libs_t_payment p
                            Where p.pledgeid = %s """,
        [id],
    )

    pledgeTotal = dictfetchall(pledgeTotal)

    totalpaid = pledgeTotal[0]["total"] if pledgeTotal else 0
    if totalpaid is None:
        totalpaid = 0

    balance = pay.amount - totalpaid

    Payform = PledgePayment(request.POST or None, request.FILES or None)
    if Payform.is_valid():
        f = Payform.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect("/pledge/%s" % id)

    context = {
        "fname": fname,
        "lname": lname,
        "rootid": pay.rootid,
        "id": pay.id,
        "currency": pay.currency,
        "amount": pay.amount,
        "purpose": pay.purpose,
        "Payform": Payform,
        "c": c,
        "pledge": pledge,
        "totalpaid": totalpaid,
        "balance": balance,
    }
    template = "pledge.html"
    return render(request, template, context)


def member_details(request, id):
    leftlinks = t_dict.objects.filter(category="leftlinks").order_by("id")
    purpose = t_dict.objects.filter(category="purpose").order_by("id")
    dictionary = t_dictionary.objects.all().order_by("id")
    lftlinks = t_urls.objects.filter(category="leftlinks").order_by("id")
    grp = t_group.objects.filter(rootid=id).order_by("-id")
    grp_list = t_dictionary.objects.all().order_by("name")

    edit_inst = get_object_or_404(t_acct, id=id)
    payments = t_payment.objects.filter(rootid=id, commitment="Cash").order_by("-id")
    pledge = t_payment.objects.filter(rootid=id, commitment="Pledge").order_by("-id")

    t = connection.cursor()
    t.cursor.execute(
        """Select
                            sum(p.amount) as amount
                            FROM libs_t_payment p
                            Where p.rootid = %s and p.commitment = 'Cash'""",
        [id],
    )

    total = dictfetchall(t)

    total = total[0]["amount"] if total else 0

    pt = connection.cursor()
    pt.cursor.execute(
        """Select
                            sum(p.amount) as amount
                            FROM libs_t_payment p
                            Where p.rootid = %s AND p.commitment = 'Pledge'""",
        [id],
    )

    ptotal = dictfetchall(pt)

    ptotal = ptotal[0]["amount"] if ptotal else 0

    child = connection.cursor()
    child.cursor.execute(
        """Select
                            *
                            FROM joins_t_children c
                            INNER JOIN joins_t_acct a ON a.id = c.childid
                            WHERE rootid = %s
                            """,
        [edit_inst.id],
    )

    child = dictfetchall(child)

    Acctform = AcctForm2(
        request.POST or None, request.FILES or None, instance=edit_inst
    )
    if Acctform.is_valid():
        f = Acctform.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        # return HttpResponseRedirect('/upload-sermon/')

    Payform = PaymentForm(request.POST or None, request.FILES or None)
    if Payform.is_valid():
        f = Payform.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        # return HttpResponseRedirect('/confirmation/')

    Groupform = GroupForm(request.POST or None, request.FILES or None)
    if Groupform.is_valid():
        f = Groupform.save(commit=False)
        f.save()
        messages.success(request, "Saved")

    PersonalGroupform = PersonalGroupForm(request.POST or None, request.FILES or None)
    if PersonalGroupform.is_valid():
        f = PersonalGroupform.save(commit=False)
        f.save()
        messages.success(request, "Saved")

    Personalfamily = AddChildrenForm(request.POST or None, request.FILES or None)
    if Personalfamily.is_valid():
        f = Personalfamily.save(commit=False)
        f.save()
        messages.success(request, "Saved")

    context = {
        "leftlinks": leftlinks,
        "lftlinks": lftlinks,
        "Acctform": Acctform,
        "Payform": Payform,
        "m_id": edit_inst.id,
        "fname": edit_inst.fname,
        "lname": edit_inst.lname,
        "gender": edit_inst.gender,
        "phone": edit_inst.phone,
        "email": edit_inst.email,
        "zone": edit_inst.zone,
        "department": edit_inst.department,
        "member_status": edit_inst.member_status,
        "years_in_ministry": edit_inst.years_in_ministry,
        "baptised": edit_inst.baptised,
        "image": edit_inst.image,
        "child": child,
        "d": dictionary,
        "payments": payments,
        "pledge": pledge,
        "total": total,
        "ptotal": ptotal,
        "PersonalGroupform": PersonalGroupform,
        "Personalfamily": Personalfamily,
        "Groupform": Groupform,
        "grp": grp,
        "grp_list": grp_list,
    }
    template = "member_details.html"
    return render(request, template, context)


def allmembers(request):
    headings = t_dictionary.objects.all().order_by("id")
    lftlinks = t_urls.objects.filter(category="leftlinks").order_by("id")
    users = User.objects.all()
    a = t_user_attribute.objects.all()

    form = FilterAcctForm()

    hlinks = connection.cursor()
    hlinks.cursor.execute(
        """Select u.id, u.icon, u.name as Hname, u.link, u.status
                            FROM siteInfo_t_urls u
                            WHERE u.status = "Active"    
                            ORDER BY -u.id
                            """
    )

    hlinks = dictfetchall(hlinks)

    t = connection.cursor()
    t.cursor.execute(
        """Select p.id,
                            a.fname as fname, 
                            a.lname as lname, p.currency as currency, p.amount as amount, p.purpose, p.commitment as commitment
                            FROM libs_t_payment p
                            INNER JOIN joins_t_acct a ON a.id = p.rootid
                            ORDER BY -p.id LIMIT 4
                            """
    )

    t = dictfetchall(t)

    s = connection.cursor()
    s.cursor.execute(
        """Select
                            sum(p.amount) as amount, p.purpose as purpose, p.currency
                            FROM libs_t_payment p
                            WHERE p.currency = 'USD'
                            Group By purpose
                            """
    )

    s = dictfetchall(s)

    queryset_list = t_acct.objects.filter().order_by("-id")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(fname__icontains=query) | Q(lname__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get("page")
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    c = connection.cursor()
    c.cursor.execute(
        """Select a.gender, count(a.id) as total
                            FROM joins_t_acct a
                            GROUP BY a.gender
                            """
    )

    c = dictfetchall(c)

    totalFemale = c[0]["total"] if c else 0
    totalMen = c[1]["total"] if c else 0
    totalCount = (totalFemale if totalFemale is not None else 0) + (
        totalMen if totalMen is not None else 0
    )

    avator = connection.cursor()
    avator.cursor.execute(
        """Select
                            au.username, u.avatar
                            FROM joins_UserProfile u
                            INNER JOIN auth_User au ON au.id = u.rootid

                            """
    )

    avator = dictfetchall(avator)

    user_p = get_object_or_404(UserProfile, rootid=request.user.id)

    img_form = AvatarForm(request.POST or None, request.FILES or None, instance=user_p)
    if img_form.is_valid():
        f = img_form.save(commit=False)
        f.save()
        messages.success(request, "Saved")

    context = {
        "user_p": user_p,
        "form": form,
        "users": avator,
        "user_avatar": user_p.avatar,
        "img_form": img_form,
        "hlinks": hlinks,
        "headings": headings,
        "lftlinks": lftlinks,
        "a": a,
        "members": queryset,
        "page_request_var": page_request_var,
        "transactions": t,
        "s": s,
        "totalFemale": totalFemale,
        "totalMen": totalMen,
        "totalCount": totalCount,
    }
    template = "all_members.html"
    return render(request, template, context)


def users(request):
    avator = connection.cursor()
    avator.cursor.execute(
        """Select
                            au.id, au.username, u.avatar
                            FROM joins_UserProfile u
                            INNER JOIN auth_User au ON au.id = u.rootid

                            """
    )

    avator = dictfetchall(avator)

    paginator = Paginator(avator, 12)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get("page")
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "users": queryset,
        "page_request_var": page_request_var,
    }

    template = "users.html"
    return render(request, template, context)


def user_details(request, id):
    dic = t_dictionary.objects.all().order_by("id")
    edit_user = get_object_or_404(UserProfile, rootid=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=edit_user)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect("/libs/user-confirmation/")

    context = {
        "form": form,
        "rootid": edit_user.rootid,
        "access_level": edit_user.access_level,
        "zone": edit_user.zone,
        "department": edit_user.department,
        "avatar": edit_user.avatar,
        "dictionary": dic,
    }

    template = "user_details.html"
    return render(request, template, context)


def user_confirmation(request):
    context = {}

    template = "user_confirmation.html"
    return render(request, template, context)


def children(request):
    leftlinks = t_dict.objects.filter(category="leftlinks").order_by("id")
    lftlinks = t_urls.objects.filter(category="leftlinks").order_by("id")
    a = t_user_attribute.objects.filter()
    row = t_children.objects.filter().order_by("division")

    row = connection.cursor()
    row.cursor.execute(
        """Select a.id, a.fname, a.lname, a.gender, a.image, ap.id as parent_id, 
                            ap.fname as parent_fname, 
                            ap.lname as parent_lname, ap.email, ap.phone, ap.site
                            FROM joins_t_children c
                            INNER JOIN joins_t_acct a ON a.id = c.childid
                            INNER JOIN joins_t_acct ap ON ap.id = c.rootid
                            """
    )

    queryset_list = dictfetchall(row)

    c = connection.cursor()
    c.cursor.execute(
        """Select a.gender, count(c.id) as total
                            FROM joins_t_children c
                            INNER JOIN joins_t_acct a ON a.id = c.childid
                            GROUP BY a.gender    
                            """
    )

    c = dictfetchall(c)

    girls = c[0]["total"] if c else 0
    boys = c[1]["total"] if c else 0
    totalCount = girls + boys

    hlinks = connection.cursor()
    hlinks.cursor.execute(
        """Select u.id, u.icon, u.name as Hname, u.link, u.status
                            FROM siteInfo_t_urls u
                            WHERE u.status = "Active" 
                            ORDER BY -u.id
                            """
    )

    hlinks = dictfetchall(hlinks)

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(fname__icontains=query) | Q(lname__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get("page")
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    form = AddChildrenForm()
    if request.is_ajax():
        form = AddChildrenForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            data = {"message": "form is saved"}
            return JsonResponse(data)

    context = {
        "girls": girls,
        "boys": boys,
        "totalCount": totalCount,
        "form": form,
        "hlinks": hlinks,
        "a": a,
        "leftlinks": leftlinks,
        "lftlinks": lftlinks,
        "members": queryset,
        "page_request_var": page_request_var,
    }
    template = "children.html"
    return render(request, template, context)


def ajax_search(request):
    context = {
        # 'members':query,
    }
    template = "all_members.html"
    return render(request, template, context)


def calendar_2(request):
    context = {
        # 'members':query,
    }
    template = "calendar.html"
    return render(request, template, context)


def member_payments(request, id):
    leftlinks = t_dict.objects.filter(category="leftlinks").order_by("id")
    lftlinks = t_urls.objects.filter(category="leftlinks").order_by("id")

    instance = get_object_or_404(t_acct, id=id)

    form = PaymentForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        # return HttpResponseRedirect('/upload-sermon/')

    context = {
        "leftlinks": leftlinks,
        "lftlinks": lftlinks,
        "form": form,
        "m_id": instance.id,
    }
    template = "member_payments.html"
    return render(request, template, context)


def upload_sermon(request):
    dictionary = t_dictionary.objects.all()

    form = SermonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect("/sermons/")

    context = {
        "form": form,
        "d": dictionary,
    }
    template = "upload_sermon.html"
    return render(request, template, context)


def add_member(request):
    cate = t_dict.objects.all().order_by("id")
    u = t_user_attribute.objects.all()

    form = AcctForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        # return HttpResponseRedirect('/confirmation/')

    context = {
        "form": form,
        "cate": cate,
        "u": u,
    }
    template = "add_member.html"
    return render(request, template, context)


def ajax_add_member(request):
    row = connection.cursor()
    row.cursor.execute(
        """Select *
                            FROM siteInfo_t_dictionary
                            """
    )

    row = dictfetchall(row)

    u = t_user_attribute.objects.all()

    form = AcctForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        # return HttpResponseRedirect('/confirmation/')

    # form = AcctForm()
    # if request.is_ajax():
    #     form = AcctForm(request.POST)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.user = request.user
    #         instance.save()
    #         data = {
    #         'message':'form is saved'
    #         }
    #         return JsonResponse(data)

    context = {
        "form": form,
        "row": row,
        "u": u,
    }
    template = "ajax_add_member.html"
    return render(request, template, context)


def confirmation(request):
    context = {}
    template = "confirmation.html"
    return render(request, template, context)


def stationary(request):
    leftlinks = t_dict.objects.filter(category="leftlinks").order_by("id")
    lftlinks = t_urls.objects.filter(category="leftlinks").order_by("id")

    row = t_stationary.objects.all().order_by("-id")

    paginator = Paginator(row, 30)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get("page")
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    stationaryform = StationaryForm(request.POST or None, request.FILES or None)
    if stationaryform.is_valid():
        f = stationaryform.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        # return HttpResponseRedirect('/confirmation/')

    context = {
        "leftlinks": leftlinks,
        "lftlinks": lftlinks,
        "stationaryform": stationaryform,
        "row": queryset,
        "page_request_var": page_request_var,
    }
    template = "stationary.html"
    return render(request, template, context)


def attendance(request):
    attendanceform = AttendanceForm(request.POST or None, request.FILES or None)
    if attendanceform.is_valid():
        f = attendanceform.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        # return HttpResponseRedirect('/confirmation/')

    context = {
        "attendance": attendanceform,
    }
    template = "attendance.html"
    return render(request, template, context)


def download_bk(request):
    response = HttpResponse(dataset.csv, content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="DailyTransactions.csv"'

    return response
