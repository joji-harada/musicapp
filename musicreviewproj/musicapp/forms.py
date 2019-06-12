from django import forms
from .models import Product, MusicType, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model=MusicType
        fields='__all__'