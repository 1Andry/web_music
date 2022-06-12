from django import forms
from django.forms import ModelForm

from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Songs, UserList


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = Songs

        fields = ('song', 'user')


class PlayListForm(forms.ModelForm):

    class Meta:
        model = UserList
        fields = ('user', 'play_list', 'songs_link')

#
#
# class LoginUserForm(forms.Form):
#     email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
