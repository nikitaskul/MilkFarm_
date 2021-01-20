from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}))
    postal_code = forms.CharField(label='Индекс', widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'form-control'}))
    paid = forms.BooleanField(label='Оплатить сейчас')

    class Meta:
        model = Order
        fields = ['name', 'email', 'address', 'postal_code', 'city', 'paid']
