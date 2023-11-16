from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Album, Artist, Song
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import AlbumForm, ArtistForm, SongForm
import webbrowser
from googleapiclient.discovery import build

API_KEY ='AIzaSyATJv1Cua9K5ZJHUvxz86caG0y5RwYNW68'
VIDEO_ID = ""

############################################################################
def song_view(request):
    # Retrieve all the data from the model
    queryset = Song.objects.all()

    # Number of items to be displayed per page
    items_per_page = 10

    # Create a Paginator object
    paginator = Paginator(queryset, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the page object from the given page number
        items = paginator.page(page)
    except PageNotAnInteger:
        # if the page is not an integer, deliver the first page
        items = paginator.page(1)
    except EmptyPage:
        # If it is out of range, deliver the last page
        items = paginator.page(paginator.num_pages)
    
    # Pass the items to your template
    return render("songs.html", {"items": items})


############################################################################

# Create your views here.
class HomeView(TemplateView):
    template_name = "artistsapp/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['songs'] = Song.objects.all()
        context['artists'] = Artist.objects.all()
        context['albums'] = Album.objects.all()

        return context

class ArtistsView(ListView):
    model = Artist
    form_class = ArtistForm
    template_name = "artistsapp/artists.html"

class UpdateArtistsView(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = "artistsapp/update_artist.html"

class DeleteArtistsView(DeleteView):
    model = Artist
    template_name = "artistsapp/delete_artist.html"
    success_url = "/artists/"

class CreateArtistsView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = "artistsapp/add_artist.html"

class AlbumsView(ListView):
    model = Album
    form_class = AlbumForm
    template_name = "artistsapp/albums.html"

class CreateAlbumsView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "artistsapp/add_album.html"

class UpdateAlbumsView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "artistsapp/update_album.html"

class DeleteAlbumsView(DeleteView):
    model = Album
    template_name = "artistsapp/delete_album.html"
    success_url = "/albums/"

class SongsView(ListView):
    model = Song
    form_class = SongForm
    template_name = "artistsapp/songs.html"

class CreateSongsView(CreateView):
    model = Song
    form_class = SongForm
    template_name = "artistsapp/add_song.html"

class SongDetailsView(DetailView):
    model = Song
    form_class = SongForm
    template_name = "artistsapp/song_details.html"

class UpdateSongsView(UpdateView):
    model = Song
    form_class = SongForm
    template_name = "artistsapp/update_song.html"

class DeleteSongsView(DeleteView):
    model = Song
    template_name = "artistsapp/delete_song.html"
    success_url = "/songs/"

def get_youtube_url(song_name):
    # api_key='AIzaSyATJv1Cua9K5ZJHUvxz86caG0y5RwYNW68'
    # Replace 'YOUR_API_KEY' with your actual API key
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Search for videos related to the song name
    search_response = youtube.search().list(
        q=song_name, 
        type='video', 
        part='id', 
        maxResults=1
        ).execute()

    # Get the video ID of the first result
    VIDEO_ID = search_response['items'][0]['id']['videoId']
    print(f"{song_name} Video ID: {VIDEO_ID}")

    # Construct the YouTube URL
    youtube_url = f"http://www.youtube.com/watch?v={VIDEO_ID}"

    return youtube_url

def song_search_view(request, query):
    return redirect(get_youtube_url(query))

# def get_video_views(video_id, api_key):
def get_video_views(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.videos().list(part='statistics', id=video_id)
    response = request.execute()

    view_count = response['items'][0]['statitics']['viewCount']
    print(f"Video views: {view_count}")
    return view_count

def video_views(request):
    view_count = get_video_views(VIDEO_ID, API_KEY)
    print(f"view_count: {view_count}")

    return render(request, {'view_count': view_count})

def artist_search_view(request, query):
    url = f"http://google.com/search?q={query}" 
    return redirect(url)

