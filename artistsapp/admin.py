from django.contrib import admin
from .models import Song, Album, Artist

# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "stage_name", "country", "dob",)
    # prepopulated_fields = {"slug": ("stage_name")}

class SongAdmin(admin.ModelAdmin):
    list_display = ("name", "album", "artist", "genre",)
    # prepopulated_fields = {"slug": ("stage_name")}

class AlbumAdmin(admin.ModelAdmin):
    list_display = ("artist", "name", "release_date",)
    # prepopulated_fields = {"slug": ("stage_name")}

admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)