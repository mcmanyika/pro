from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

from libs.models import *
from joins.models import *

class SermonForm(forms.ModelForm):
    class Meta:
        model = t_sermon
        fields = ['title',
                  'event',
                  'venue',
                  'preacher',
                  'audio',
                  'video',
                  'notes',
                  'user',
                  ]
class FilterAcctForm(forms.ModelForm):
    class Meta:
        model = t_acct
        fields = ['fname'
                  ]

class AcctForm(forms.ModelForm):
    class Meta:
        model = t_acct
        fields = ['fname',
                  'lname',
                  'gender',
                  'user',
                  ]

yim = [(i, str(i)) for i in range(1, 26)]

class AcctForm2(forms.ModelForm):
    fname = forms.CharField(max_length=30, required=False, widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'First Name'}), label= False)
    lname = forms.CharField(max_length=30, required=False, widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'Last Name'}), label= False)
    
    
    phone = forms.CharField(max_length=30, required=False, widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'+263 333 3333'}), label= False)
    email = forms.CharField(required=False, widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'Email'}), label= False)
    department = forms.CharField(required=False, widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'Department'}), label= False)
    years_in_ministry = forms.TypedChoiceField(choices=yim, coerce=int, label= False)
    
    
    class Meta:
        model = t_acct
        fields = ('fname',
                  'lname',
                  'gender',
                  'phone',
                  'email',
                  'zone',
                  'department',
                  'member_status',
                  'years_in_ministry',
                  'baptised',
                  'image',
                  'user',
                  )                  

class PaymentForm(forms.ModelForm):
    class Meta:
        model = t_payment
        fields = ['rootid',
                  'currency',
                  'amount',
                  'purpose',
                  'commitment',
                  'ref',
                  'user',
                  ]

class SeedPaymentForm(forms.ModelForm):
    class Meta:
        model = t_payment
        fields = ['currency',
                  'amount',
                  'purpose',
                  'commitment',
                  'ref',
                  'user',
                  ]

class PledgePayment(forms.ModelForm):
    class Meta:
        model = t_payment
        fields = [
                  'rootid',
                  'pledgeid',
                  'currency',
                  'amount',
                  'purpose',
                  'commitment',
                  'ref',
                  'user',
                  ]                  

class StationaryForm(forms.ModelForm):
    class Meta:
        model = t_stationary
        fields = ['name',
                  'img',
                  'category',
                  ]  

class AddChildrenForm(forms.ModelForm):
    class Meta:
        model = t_children
        fields = ['rootid',
                  'childid',
                  'relationship',
                  ] 


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = t_attendance
        fields = ['rootid',
                  'zone',
                  'service',
                  'user',
                  ] 




