from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('profile/', user_p, name='profile'),
    path('test/', test, name='test'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('upload/', add_song, name='add_song'),
    path('logout/', auth_views.LogoutView.as_view(template_name='player/logout.html'), name='logout'),
    path('intro/', auth_views.LogoutView.as_view(template_name='player/intro.html')),
]
