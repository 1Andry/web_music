from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, blank=True)
    password = models.CharField(max_length=50, blank=True)
    time_created = models.DateTimeField(auto_now=True)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'


class Songs(models.Model):
    song = models.FileField(upload_to='uploads/songs', blank=True, unique=True, validators=[
        FileExtensionValidator(allowed_extensions=['mp3'], message='только mp3 формат')])
    user = models.ForeignKey(User, blank=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.song)

    class Meta:
        verbose_name = 'песни'
        verbose_name_plural = 'песни'


class UserList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь' )
    play_list = models.CharField(max_length=115, verbose_name='название плейлиста')
    songs_link = models.ManyToManyField('Songs', blank=True, verbose_name='songs_link')

    def __str__(self):
        return str(self.user)
