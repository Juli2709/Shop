from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


# TODO форма для оформления после заказа
class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    address = forms.CharField(label='Адрес доставки', widget=forms.TextInput(
        attrs={'class': 'form-control', "rows": 3}))
    phone = forms.IntegerField(label='Номер телефона в формате +375 ** *******', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    comment = forms.CharField(label='Комментарий к заказу', widget=forms.Textarea(
        attrs={'class': 'form-control', "rows": 3}))


# TODO форма для введения логина/пароля
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


# TODO форма для регистрации
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
