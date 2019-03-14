from django import forms
from django.forms import ModelForm
from .models import Product


#class ProductForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=255)
#     price = forms.FloatField(label='Price', max_value=5)
#     stack = forms.IntegerField(label='Stack', max_value=500)
#     image_url = forms.CharField(label='Image URL', max_length=2083)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stack', 'image_url']


class LoginForm(forms.Form):
    username =  forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())


