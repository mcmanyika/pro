from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from finance.models import *


class IncomeHeadForm(forms.ModelForm):
    class Meta:
        model = t_dict
        fields = [
            "name",
            "category",
            "user_id",
        ]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = t_payment
        fields = [
            "rootid",
            "currency",
            "amount",
            "purpose",
            "commitment",
            "ref",
            "user",
        ]


class SeedPaymentForm(forms.ModelForm):
    class Meta:
        model = t_payment
        fields = [
            "currency",
            "amount",
            "purpose",
            "commitment",
            "ref",
            "user",
        ]


class PledgePayment(forms.ModelForm):
    class Meta:
        model = t_payment
        fields = [
            "rootid",
            "pledgeid",
            "currency",
            "amount",
            "purpose",
            "commitment",
            "ref",
            "user",
        ]
