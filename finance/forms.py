from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import *



class IncomeHeadForm(forms.ModelForm):
    class Meta:
        model = t_dict
        fields = [
        			'name',
        			'category',
        			'user_id',

        		]



