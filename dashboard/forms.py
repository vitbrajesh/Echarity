from django import forms
from django.contrib.auth.models import User
from dashboard.models import Document 


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
    firstname = forms.CharField(
        label='Enter your first name',
    )
    lastname = forms.CharField(
        label='Enter your last name',
    )
    address = forms.CharField(
        label='Enter your address',
    )


