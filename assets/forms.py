from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

from assets.models import *


class NewAssetForm(forms.ModelForm):
    class Meta:
        model = t_assets
        fields = ['rootid',
                  'name',
                  'serial_no',
                  'department',
                  'zone',
                  'equip_type',
                  'user',
                  ]