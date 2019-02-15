from django import forms
from siteInfo.models import *



# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = t_contact
#         fields = ["root_id","email","title", "message"]

class TitleForm(forms.ModelForm):
    class Meta:
        model = t_dictionary
        fields = ["name"]
