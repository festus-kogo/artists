from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("songs/", views.SongsView.as_view(), name="songs"),
    path("songs/create/", views.CreateSongsView.as_view(), name="add_song"),
    path("songs/<pk>/update/", views.UpdateSongsView.as_view(), name="update_song"),
    path("songs/<pk>/delete/", views.DeleteSongsView.as_view(), name="delete_song"),
    path("songs/search/<str:query>/", views.song_search_view, name="song_search"),
    # path("songs/<pk>/details/", views.SongDetailsView.as_view(), name="song_details"),

    path("artists/", views.ArtistsView.as_view(), name="artists"),
    path("artists/create/", views.CreateArtistsView.as_view(), name="add_artist"),
    path("artists/<pk>/update/", views.UpdateArtistsView.as_view(), name="update_artist"),
    path("artists/<pk>/delete/", views.DeleteArtistsView.as_view(), name="delete_artist"),
    path("artists/search/<str:query>/", views.artist_search_view, name="artist_search"),

    path("albums/", views.AlbumsView.as_view(), name="albums"),    
    path("albums/create/", views.CreateAlbumsView.as_view(), name="add_album"),
    path("albums/<pk>/update/", views.UpdateAlbumsView.as_view(), name="update_album"),
    path("albums/<pk>/delete/", views.DeleteAlbumsView.as_view(), name="delete_album"),

]