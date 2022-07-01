from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import AlbumForm, SongForm, UserForm
from .models import Album, Song

AUDIO_FILE_TYPES = ['wav', 'mp3']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_album(request):
    if not request.user.is_authenticated:
        return render(request, 'player/login.html')
    else:
        form = AlbumForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            if not album.album_logo:
                album.album_logo = 'static/nones.png'
                album.album_logo = request.FILES['album_logo']
                file_type = album.album_logo.url.split('.')[-1]
                file_type = file_type.lower()
                if file_type not in IMAGE_FILE_TYPES:
                    context = {
                        'album': album,
                        'form': form,
                        'error_message': 'Image file must be PNG, JPG, or JPEG',
                    }
                    return render(request, 'player/create_album.html', context)
            album.save()
            return render(request, 'player/detail.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'player/create_album.html', context)


def create_song(request, album_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        song = form.save(commit=False)
        song.album = album
        song.audio_file = request.FILES['audio_file']
        file_type = song.audio_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context = {
                'album': album,
                'form': form,
                'error_message': 'Audio file must be WAV, MP3, or OGG',
            }
            return render(request, 'player/create_song.html', context)

        song.save()
        return render(request, 'player/detail.html', {'album': album})
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'player/create_song.html', context)


def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    album.delete()
    albums = Album.objects.filter(user=request.user)
    return render(request, 'player/index.html', {'albums': albums})


def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'player/detail.html', {'album': album})


def detail(request, album_id):
    if not request.user.is_authenticated:
        return render(request, 'player/login.html')
    else:
        user = request.user
        album = get_object_or_404(Album, pk=album_id)
        return render(request, 'player/detail.html', {'album': album, 'user': user})


@login_required
def favorite(request):
    favorite_songs = Song.objects.filter(is_favorite=request.user)
    return render(request, 'player/favorite.html', {'favorite_songs': favorite_songs})


@login_required
def favorite_add(request, pk):
    song = get_object_or_404(Song, pk=request.POST.get('song_id'))
    song.is_favorite.add(request.user)
    return redirect('player:songs')


@login_required
def favorite_remove(request, pk):
    song = get_object_or_404(Song, pk=request.POST.get('song_id'))
    song.is_favorite.remove(request.user)
    return redirect('player:favorite')


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'player/login.html')
    else:
        albums = Album.objects.filter(user=request.user)
        song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
                Q(album_title__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()
            song_results = song_results.filter(
                Q(song_title__icontains=query)
            ).distinct()
            return render(request, 'player/index.html', {
                'albums': albums,
                'songs': song_results,
            })
        else:
            return render(request, 'player/index.html', {'albums': albums})


def logout_user(request):
    logout(request)
    return render(request, 'player/logout_user.html')


def login_user(request):
    if request.method == "GET":
        return render(request, 'player/login.html', {'form': AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'player/index.html', {'albums': albums})
            else:
                return render(request, 'player/login.html',
                              {'error': 'Неверные данные для входа  ', 'form': AuthenticationForm()})
        else:
            return render(request, 'player/login.html', {'error': 'Неверные данные для входа '})


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        if password1 == password2:
            user.set_password(password1)
            user.save()
            user = authenticate(username=username, password=password1)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'player/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'player/register.html', context)


def songs(request, ):
    favorite_songs = Song.objects.filter(is_favorite=request.user)
    print(favorite_songs)
    if not request.user.is_authenticated:
        return render(request, 'player/login.html')
    else:
        try:
            song_ids = []
            for album in Album.objects.filter(user=request.user):
                for song in album.song_set.all():
                    song_ids.append(song.pk)
            users_songs = Song.objects.filter(pk__in=song_ids)
        except Album.DoesNotExist:
            users_songs = []
        return render(request, 'player/songs.html', {
            'song_list': users_songs,
            'favorite_songs': favorite_songs,
        })
