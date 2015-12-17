from django import forms
from django.contrib.auth.models import User
from products.models import Product
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 


class PostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'active', 'quantity','address', 'zip_Code', 'expire_date', )



class DocumentForm(forms.Form):
    
    title = forms.CharField(
        label='Title',
    )
    
    description = forms.CharField(
        label='Description',
    )   
   
    active = forms.BooleanField(
        label='Active',
    )
    quantity = forms.IntegerField(
        label='Quantity',
    )
    zip_Code = forms.CharField(
        label='Zip_Code',
    )
    docfile = forms.FileField(
        label='Select  Your Product Image (Image can not be update in future)',
    )
    address = forms.CharField(
        label='Address',
    )
    expire_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    
    
    
