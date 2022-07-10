from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'player'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('<int:album_id>/', detail, name='detail'),
    path('songs/favorite/', favorite, name='favorite'),
    path('fav/<int:pk>/', favorite_add, name='favorite_add'),
    path('fa/<int:pk>/', favorite_remove, name='favorite_remove'),
    path('songs/', songs, name='songs'),
    path('create_album/', create_album, name='create_album'),
    path('<int:album_id>/create_song/', create_song, name='create_song'),
    path('<int:album_id>/delete_song/<int:song_id>/', delete_song, name='delete_song'),
    path('<int:album_id>/delete_album/', delete_album, name='delete_album'),
    path('search/', search, name='search'),
]
