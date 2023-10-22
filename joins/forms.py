from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from joins.models import UserProfile, t_acct
from siteInfo.models import *
from django import *
from django.contrib.auth import authenticate, get_user_model, login, logout

from .models import *

User = get_user_model()


class EmailForm(forms.Form):
    email = forms.EmailField()


class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ["email"]


class JoinForm2(forms.ModelForm):
    class Meta:
        model = Join
        fields = ["email"]


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ["email"]


class AvatarForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["rootid", "avatar"]


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "rootid",
            "department",
            "access_level",
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "rootid",
            "zone",
            "department",
            "avatar",
            "access_level",
        ]


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label="Email address")
    email2 = forms.EmailField(label="Confirm Email")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "email2",
            "password",
        ]

    def clean_email2(self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email != email2:
            raise forms.ValidationError("Emails must match")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email


class AttriForm(forms.ModelForm):
    class Meta:
        model = t_user_attribute
        fields = [
            "root",
            "department",
            "level",
            "status",
        ]


class GroupForm(forms.ModelForm):
    class Meta:
        model = t_dictionary
        fields = [
            "name",
            "category",
            "sub_category",
            "user",
        ]


class PersonalGroupForm(forms.ModelForm):
    class Meta:
        model = t_group
        fields = [
            "rootid",
            "name",
            "category",
            "user",
        ]


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-sm", "placeholder": "Username"}
        ),
        label="",
    )

    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-sm", "placeholder": "First Name"}
        ),
        label="",
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-sm", "placeholder": "Last Name"}
        ),
        label="",
    )
    email = forms.EmailField(
        max_length=254,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-sm", "placeholder": "Email"}
        ),
        label="",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control form-control-sm", "placeholder": "Password"}
        ),
        label="",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Repeat Password",
            }
        ),
        label="",
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class UserAttributeForm(forms.ModelForm):
    GENDER_OPTIONS = (
        ("Female", "Female"),
        ("Male", "Male"),
    )
    ZONE_OPTIONS = (
        ("IOC", "IOC"),
        ("UAE", "UAE"),
    )
    gender = forms.ChoiceField(
        choices=GENDER_OPTIONS,
        required=True,  # Set this to True if user_type is required
        widget=forms.Select(
            attrs={"class": "form-control custom-padding form-control-lg"}
        ),
        label="Gender",
    )
    marital_status = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Marital status",
            }
        ),
        label="",
    )
    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-sm", "placeholder": "Phone"}
        ),
        label="",
    )

    member_status = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Member Status",
            }
        ),
        label="",
    )
    baptised = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-sm", "placeholder": "Baptised"}
        ),
        label="",
    )

    class Meta:
        model = t_acct
        fields = [
            "root",
            "user",
            "gender",
            "dob",
            "marital_status",
            "phone",
            "member_status",
            "baptised",
        ]
