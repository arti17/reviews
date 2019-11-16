from django import forms
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class ReviewProductForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['author', 'product']
