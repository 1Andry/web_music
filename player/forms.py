from django import forms
from django.contrib.auth.models import User

from .models import Album, Song


class AlbumForm(forms.ModelForm):
    # album_title = forms.CharField(label='Название', max_length=500)
    # album_logo = forms.ImageField(label='Логотип',)

    class Meta:
        model = Album
        fields = ['album_title', 'album_logo']


class SongForm(forms.ModelForm):
    audio_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Song
        fields = ['audio_file']


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
