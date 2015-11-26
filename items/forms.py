from django import forms

from products.models import Product

class PostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'quentity', 'zipcode', 'discription', 'address')
