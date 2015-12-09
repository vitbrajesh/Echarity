from django import forms
from products.models import Product, ProductImage

class PostForm(forms.ModelForm):

    class Meta:
        model = Product 
        fields = ('title', 'description', 'price', 'active', 'quantity','address', 'zip_Code', 'date_created', 'date_Update', 'expire_date', )



class PostImgForm(forms.ModelForm):
  
    class Meta:
        model = ProductImage
        fields = ('product','image', )

     
        
