from django.contrib import admin
from .models import *


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'audio_file', 'is_favorite')
    list_display_links = ('id', 'audio_file',)
    search_fields = ('audio_file',)


admin.site.register(Album)
admin.site.register(Song, SongAdmin)
