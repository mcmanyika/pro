# import requests
import json
import math
from django.db import connection
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, Http404
from .forms import EmailForm, JoinForm, JoinForm2, UserRegisterForm
from .models import Join
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Count
from joins.forms import User
from django.contrib.auth.decorators import login_required
from siteInfo.models import *
from joins.forms import *
import uuid
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _

# Create your views here.


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    form2 = JoinForm2(request.POST or None)

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    user_p = get_object_or_404(UserProfile, rootid=request.user.id)
                except Http404:
                    return redirect("user-img")
                try:
                    user_attributes = get_object_or_404(
                        t_user_attribute, root=request.user.id
                    )

                except Http404:
                    return redirect("register-user-attributes")

                if user_p.department == "Media":
                    return HttpResponseRedirect("/allmembers/")

                else:
                    return HttpResponseRedirect("/allmembers/")

            else:
                messages.success(request, "Enter correct username or password")

    if request.method == "POST":
        passchange = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            passchange_user = user.save()
            update_session_auth_hash(request, user)
            messages.success(request, _("Your password was successfully updated!"))
            return redirect("change_password")
        else:
            messages.error(request, _("Please correct the error below."))
    else:
        passchange = PasswordChangeForm(request.user)

    context = {
        "form": form,
        "form2": form2,
        "passchange": passchange,
    }
    return render(request, "login.html", context)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("user-img")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def user_img(request):
    img_form = AvatarForm(request.POST or None, request.FILES or None)
    if img_form.is_valid():
        f = img_form.save(commit=False)
        f.save()
        # messages.success(request, "Saved")
        return redirect("register-user-attributes")

    context = {
        "img_form": img_form,
    }
    template = "user_img.html"
    return render(request, template, context)


def RegisterUserAttributes(request):
    headings = t_dictionary.objects.all()
    form = UserAttributeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        messages.success(request, "Saved")
        return redirect("home")

    context = {
        "form": form,
        "headings": headings,
    }
    template = "joins/RegisterUserAttributes.html"

    return render(request, template, context)


def signup_confirmation(request):
    return render(request, "signup_confirmation.html")


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _("Your password was successfully updated!"))
            return redirect("change_password")
        else:
            messages.error(request, _("Please correct the error below."))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {"form": form})


def Logout(request):
    logout(request)
    return redirect("/login/")
