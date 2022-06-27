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
    path('favorite/', favorite, name='favorite'),
    path('songs/<str:filter_by>/', songs, name='songs'),
    path('create_album/', create_album, name='create_album'),
    path('<int:album_id>/create_song/', create_song, name='create_song'),
    path('<int:album_id>/delete_song/<int:song_id>/', delete_song, name='delete_song'),
    path('<int:album_id>/favorite_album/', favorite_album, name='favorite_album'),
    path('<int:album_id>/delete_album/', delete_album, name='delete_album'),

]
