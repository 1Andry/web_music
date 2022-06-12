from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, CreateView, FormView, ListView, TemplateView
from django.urls import reverse_lazy
from .models import Profile, Songs, UserList
from .forms import UploadFileForm, RegisterUserForm, PlayListForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import os.path


def base(request):
    try:
        play_list = UserList.objects.filter(user=request.user)
        songs = Songs.objects.filter(user=request.user)
        return render(request, 'player/base.html', {'songs': songs, 'play_list': play_list})
    except:
        return render(request, 'player/base.html')

def test(request):
    p = UserList.objects.filter(user=request.user)
    # l = UserList.user.all()
    return render(request, 'player/test.html',{'p': p,  })



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'player/register.html'
    success_url = reverse_lazy('base')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    # def form_valid(self, form):
    #     user = form.save
    #     login(self.request, user)
    #     return redirect('base')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'player/login.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


def add_song(request):
    if request.method == 'POST':
        song = UploadFileForm(request.POST, request.FILES)
        if song.is_valid():
            song.save()
            return redirect('base')
    else:
        song = UploadFileForm()
    return render(request, 'player/upload.html', {'song': song})


def user_p(request):
    songs = Songs.objects.filter(user=request.user)
    load_song = UploadFileForm()
    play_list = PlayListForm
    # print(Songs.song)
    dict_obj = {
        'play_list': play_list,
        'songs': songs,
        'load_song': load_song,
    }
    if request.method == 'POST' and 'upload' in request.POST:
        load_song = UploadFileForm(request.POST, request.FILES)
        if load_song.is_valid():
            load_song.user = request.user
            load_song.save()
            return redirect('profile')
        else:
            print('NO')
            return render(request, 'player/profile.html', dict_obj)

    if request.method == 'POST' and 'add' in request.POST:
        play_list = PlayListForm(request.POST)
        if play_list.is_valid():
            play_list.save()
            print('YES')
            return redirect('base')
        else:
            print('NO')
            return render(request, 'player/profile.html', dict_obj)
    return render(request, 'player/profile.html', dict_obj)
