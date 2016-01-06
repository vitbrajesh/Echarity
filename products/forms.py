from django import forms
from django.contrib.auth.models import User
from products.models import Product, Service
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 


class PostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'active', 'quantity', 'address', 'zip_Code', 'expire_date', )

class Service1Form(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('title', 'description', 'active', 'duraction', 'address', 'zip_Code', 'expire_date', )

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
    expire_date = forms.DateTimeField(
        label='Expire Date',
    )
 
class ServiceForm(forms.Form):
    
    title = forms.CharField(
        label='Title',
    )
    
    description = forms.CharField(
        label='Description',
    )   
   
    active = forms.BooleanField(
        label='Active',
    )
    duraction = forms.CharField(
        label='duraction',
    )
    zip_Code = forms.CharField(
        label='Zip_Code',
    )
    address = forms.CharField(
        label='Address',
    )
    expire_date = forms.DateTimeField(
        label='Expire Date',
    )
    
