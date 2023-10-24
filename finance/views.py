# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import xlwt
import json
import math
import csv
from django.utils.encoding import smart_str
from django.utils.datastructures import MultiValueDictKeyError

# from libs.base import Base
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.http import StreamingHttpResponse
from django.db import connection
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, Http404
from datetime import datetime, date
import hashlib
import string
from django.forms import DateField, IntegerField, CharField
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# from libs.base import Base
from joins.models import *
from joins.forms import *
from libs.models import *
from libs.forms import *
from .forms import *
from finance.models import *
from .resources import DailyTransactions
from siteInfo.models import t_dictionary

# Create your views here.


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def ajax_incomehead(request):
    form = IncomeHeadForm()
    if request.is_ajax():
        form = IncomeHeadForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            data = {"message": "form is saved"}
            return JsonResponse(data)
    context = {
        "form": form,
    }
    template = "add_incomehead.html"
    return render(request, template, context)


def ajax_currency(request):
    form = IncomeHeadForm()
    if request.is_ajax():
        form = IncomeHeadForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            data = {"message": "form is saved"}
            return JsonResponse(data)
    context = {
        "form": form,
    }
    template = "add_currency.html"
    return render(request, template, context)


def ajax_commitment(request):
    form = IncomeHeadForm()
    if request.is_ajax():
        form = IncomeHeadForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            data = {"message": "form is saved"}
            return JsonResponse(data)
    context = {
        "form": form,
    }
    template = "add_commitment.html"
    return render(request, template, context)


def ajax_group(request):
    form = GroupForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")

    context = {
        "form": form,
    }
    template = "add_group.html"
    return render(request, template, context)


def transaction(request, id):
    weekly = t_dictionary.objects.filter(category="weekly")
    monthly = t_dictionary.objects.filter(category="monthly")
    onceoff = t_dictionary.objects.filter(category="onceoff")
    d = t_dictionary.objects.all().order_by("id")
    rw = t_dict.objects.all().order_by("name")

    instance = get_object_or_404(t_acct, root=id)

    member = get_object_or_404(User, id=instance.root)
    rendered = 0
    total = 0
    Payform = PaymentForm(request.POST or None, request.FILES or None)
    if Payform.is_valid():
        f = Payform.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect("/finance/receipt/%s" % instance.id)

    context = {
        "Payform": Payform,
        "d": d,
        "rw": rw,
        "member_id": instance.root,
        "first_name": member.first_name,
        "last_name": member.last_name,
        # "image": instance.image,
        "gender": instance.gender,
        "rendered": rendered,
        "total": total,
        "weekly": weekly,
        "monthly": monthly,
        "onceoff": onceoff,
    }
    template = "upload_transaction.html"
    return render(request, template, context)


def all_receipts(request, id):
    t = t_payment.objects.raw(
        """SELECT p.id,
            a.first_name, 
            a.last_name, p.currency as currency, 
            p.amount as amount, p.purpose, p.commitment as commitment
            FROM finance_t_payment p
            INNER JOIN auth_user a ON a.id = p.root
            WHERE p.root = %s  
            order by p.id desc""",
        [id],
    )

    context = {
        "rc": t,
    }
    template = "all_receipts.html"
    return render(request, template, context)


def receipt(request, id):
    receipt = t_payment.objects.raw(
        """SELECT p.id, 
                            a.first_name, 
                            a.last_name, p.currency as currency, 
                            p.amount as amount, p.purpose, p.commitment as commitment
                            FROM finance_t_payment p
                            INNER JOIN auth_user a ON a.id = p.rootid
                            WHERE p.rootid = %s  
                            order by p.pk desc limit 1""",
        [id],
    )

    all_rec = t_payment.objects.raw(
        """SELECT p.id,
                            a.first_name, 
                            a.last_name, p.currency as currency, 
                            p.amount as amount, p.purpose, p.commitment as commitment
                            FROM finance_t_payment p
                            INNER JOIN auth_user a ON a.id = p.rootid
                            WHERE p.id = %s  
                            order by p.id desc""",
        [id],
    )

    context = {
        "rc": receipt,
        "all_rec": all_rec,
        "client_id": id,
    }
    template = "receipt.html"
    return render(request, template, context)


def single_rec(request, id):
    single_rec = t_payment.objects.raw(
        """SELECT p.id, a.id as acct_id,
                            a.first_name, 
                            a.last_name, p.currency as currency, 
                            p.amount as amount, p.purpose, p.commitment as commitment
                            FROM finance_t_payment p
                            INNER JOIN auth_user a ON a.id = p.rootid
                            WHERE p.id = %s  
                            order by p.id desc""",
        [id],
    )
    for rw in single_rec:
        rw.acct_id

    context = {
        "single_rec": single_rec,
        "acct_id": rw.acct_id,
    }
    template = "entry_receipt.html"
    return render(request, template, context)


def seed_payments(request):
    leftlinks = t_dict.objects.filter(category="leftlinks").order_by("id")
    lftlinks = t_urls.objects.filter(category="leftlinks").order_by("id")
    raw = t_dict.objects.all().order_by("name")
    # instance = get_object_or_404(t_acct, id=id)

    Seedform = PaymentForm(request.POST or None, request.FILES or None)
    if Seedform.is_valid():
        f = Seedform.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect("/finance/all-seeds/")

    context = {
        "leftlinks": leftlinks,
        "lftlinks": lftlinks,
        "form": Seedform,
        "raw": raw,
    }
    template = "seed_payment.html"
    return render(request, template, context)


def all_seeds(request):
    row = t_payment.objects.all().order_by("-id")

    paginator = Paginator(row, 15)  # Show 25 contacts per page
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
        "row": queryset,
        "page_request_var": page_request_var,
    }
    template = "all_seeds.html"

    return render(request, template, context)


def seed_receipt(request, id):
    instance = get_object_or_404(t_payment, id=id)

    context = {
        "purpose": instance.purpose,
        "currency": instance.currency,
        "amount": instance.amount,
        "commitment": instance.commitment,
        "ref": instance.ref,
        "timestamp": instance.timestamp,
    }
    template = "seed_receipt.html"
    return render(request, template, context)


def filter_trans(request):
    try:
        fdate = request.POST["period_from"]
        tdate = request.POST["period_to"]

    except:
        fdate = datetime.now().date()
        tdate = datetime.now().date()

    report = connection.cursor()
    report.cursor.execute(
        """Select 
            p.purpose as PURPOSE,
            sum(case when p.currency = 'BOND' then p.id else 0 end) as BOND,
            sum(case when p.currency = 'USD' then p.id else 0 end) as USD,
            sum(case when p.currency = 'RAND' then p.id else 0 end) as RAND,
            sum(case when p.currency = 'PULA' then p.id else 0 end) as PULA,
            sum(case when p.currency = 'Dirhams' then p.id else 0 end) as DIRHAMS,
            p.timestamp as TIMESTAMP
            FROM finance_t_payment p
                WHERE p.timestamp BETWEEN %s AND %s
            GROUP BY p.purpose
            """,
        [fdate, tdate],
    )

    report = dictfetchall(report)

    def export_data(request):
        filename = filter_trans()
        trans_resource = report()
        dataset = trans_resource.export()
        response = HttpResponse(dataset.csv, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="DailyTransactions.csv"'
        return response

    context = {
        "transactions": report,
    }
    return render(request, "filter_transactions.html", context)


def export_data(request):
    trans_resource = DailyTransactions()
    dataset = trans_resource.export()
    response = HttpResponse(dataset.csv, content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="DailyTransactions.csv"'
    return response


def filter_income_head(self):
    if self.method == "POST":
        fdate = request.POST["period_from"]
        tdate = request.POST["period_to"]

    s = connection.cursor()
    s.cursor.execute(
        """Select
                            p.currency as currency, sum(p.amount) as amount, p.purpose as purpose, 
                            p.commitment as commitment
                            FROM finance_t_payment p
                            Group By p.currency, purpose, commitment
                            """
    )

    ihead = dictfetchall(s)

    context = {
        "ihead": ihead,
    }
    return render(self, "filter_by_income_head.html", context)


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def csv_view(request):
    t = connection.cursor()
    t.cursor.execute(
        """Select
                            a.first_name, 
                            a.last_name, p.currency as currency, p.amount as amount, p.purpose, 
                            p.commitment as commitment
                            FROM finance_t_payment p
                            INNER JOIN auth_User a ON a.id = p.rootid
                            ORDER BY -p.id 
                            """
    )

    t = dictfetchall(t)

    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.

    rows = (["".format(idx), str(idx)] for idx in t)
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse(
        (writer.writerow(row) for row in rows), content_type="text/csv"
    )
    response["Content-Disposition"] = 'attachment; filename="somefilename.csv"'

    return response


def get_one_row(sql="", prms=tuple()):
    found = tuple()
    if not sql:
        return found

    try:
        csr = connection.cursor()

        if prms:
            csr.execute(sql, prms)
        else:
            csr.execute(sql)

        found = csr.fetchone()
    except:
        found = tuple()

    return found
