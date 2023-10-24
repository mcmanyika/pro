from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

from libs.models import *
from joins.models import *


class SermonForm(forms.ModelForm):
    class Meta:
        model = t_sermon
        fields = [
            "title",
            "event",
            "venue",
            "preacher",
            "audio",
            "video",
            "notes",
            "user",
        ]


class FilterAcctForm(forms.ModelForm):
    class Meta:
        model = t_acct
        fields = ["fname"]


class AcctForm(forms.ModelForm):
    class Meta:
        model = t_acct
        fields = [
            "fname",
            "lname",
            "gender",
            # "user_id",
        ]


yim = [(i, str(i)) for i in range(1, 26)]


class AcctForm2(forms.ModelForm):
    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "+263 333 3333",
            }
        ),
        label=False,
    )
    department = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-sm", "placeholder": "Department"}
        ),
        label=False,
    )

    class Meta:
        model = t_acct
        fields = (
            "root",
            "user",
            "gender",
            "dob",
            "phone",
            "department",
            "member_status",
            "baptised",
        )


class StationaryForm(forms.ModelForm):
    class Meta:
        model = t_stationary
        fields = [
            "name",
            "img",
            "category",
        ]


class AddChildrenForm(forms.ModelForm):
    class Meta:
        model = t_children
        fields = [
            "rootid",
            "childid",
            "relationship",
        ]


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = t_attendance
        fields = [
            "rootid",
            "zone",
            "service",
            "user",
        ]
