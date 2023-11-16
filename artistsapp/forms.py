from .models import Album, Artist, Song
from django import forms

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = "__all__"

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = "__all__"

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = "__all__"