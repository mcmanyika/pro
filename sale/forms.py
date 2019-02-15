from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

from sale.models import *

class SaleForm(forms.ModelForm):
    class Meta:
        model = t_sale
        fields = ['rootid',
                  'price',
                  'qty',
                  ]
