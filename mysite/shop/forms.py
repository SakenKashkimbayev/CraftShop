from django import forms

from shop.models import Product


class AddProductForms(forms.ModelForm):
    # name = forms.CharField(label='Название')
    # description = forms.CharField(label='Описание')
    # price = forms.DecimalField(label='Цена')
    # category = forms.CharField(label='Категория')
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']