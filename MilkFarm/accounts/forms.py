from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings

from users.forms import CustomUserCreationForm
from users.models import User

from users import aes


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(CustomUserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Повторите новый пароль',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserEmailChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class UserAdditionalInfoChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'date_of_birth', 'phone_number', 'address', 'about', 'company']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserPaymentDetailsChangeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserPaymentDetailsChangeForm, self).__init__(*args, **kwargs)

        if self.instance.card_number != '':
            decode_card_number = bytes.decode(aes.decrypt(aes.make_dict_from_str(self.instance.card_number),
                                                          settings.PASSWORD_AES))
            # self.instance.card_number = '****-****-****-' + decode_card_number[-4:]
            self.instance.card_number = decode_card_number

            kwargs['instance'] = self.instance
            super(UserPaymentDetailsChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['card_number']
        widgets = {
            'card_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_card_number(self):
        if self.cleaned_data['card_number'] != '':
            card_number = self.cleaned_data['card_number']
            return aes.make_str_from_dict(aes.encrypt(card_number, settings.PASSWORD_AES))
        else:
            return ''


class UserAddMoney(forms.ModelForm):
    class Meta:
        model = User
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }