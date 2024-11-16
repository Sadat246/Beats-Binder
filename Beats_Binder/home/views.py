from django.shortcuts import render
import requests
import json
import os
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from artists.models import Artist
from albums.models import Album
from songs.models import Song

# Create your views here.

from .search_form import SearchForm

def home_view(request):
    absolute_path = os.path.dirname(os.path.abspath(__file__))

    artists_data = open(absolute_path + '/json/top_artists.json')
    top_artists = json.load(artists_data)
    artists_data.close()

    albums_data = open(absolute_path + '/json/top_albums.json')
    top_albums = json.load(albums_data)
    albums_data.close()

    tracks_data = open(absolute_path + '/json/top_tracks.json')
    top_tracks = json.load(tracks_data)
    tracks_data.close()
    return render(request, 'home/home.html', 
                  context={'top_artists': top_artists,
                          'top_albums': top_albums,
                          'top_tracks': top_tracks,
                          'search_form': SearchForm})

def search_results_view(request):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm
        return context
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            search_input = form.cleaned_data["Search"]
            search_result = searchAPI(search_input)
            # for i in range(len(search_result["data"])):
                # print(search_result["data"][i])
            return render(request, "home/search_results.html", context={"search_result": search_result["data"],
                                                                        "search_input": search_input,
                                                                        "search_form": form})
    if request.method == 'POST':
        # modifyAlbumSaved(list(request.POST.keys())[1])
        ids = list(request.POST.keys())[1].split(" ")
        saveSong(ids[0])
        saveArtist(ids[1])
        saveAlbum(ids[2])
    else: 
        form = SearchForm()
    return render(request, "home/search_results.html", 
            context={'search_form': SearchForm})
    
def searchAPI(search_input):
    url = "https://deezerdevs-deezer.p.rapidapi.com/search"
    querystring = {"q": search_input}
    headers = {
        "X-RapidAPI-Key": "de8f6f2a3fmsh850207b34ede80bp17e3d8jsnd9883430d914",
        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    search_results = response.json()
    return search_results

def addArtistEntry(deezerID, saved):
    if not Artist.objects.filter(deezer_id=deezerID).exists():
        url = "https://deezerdevs-deezer.p.rapidapi.com/artist/" + str(deezerID)
        headers = {
        "X-RapidAPI-Key": "dc2e72cb1cmsh271df14842a824bp190aaajsnf4720429b177",
        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers).json()
        name = response["name"]
        cover = response["picture_small"]
        nb_album = response["nb_album"]
        Artist.objects.create(deezer_id=deezerID,name=name,cover=cover,nb_album=nb_album,saved=saved).save()

def addAlbumEntry(deezerID,saved):
    if not Album.objects.filter(deezer_id=deezerID).exists():
        url = "https://deezerdevs-deezer.p.rapidapi.com/album/" + str(deezerID)
        headers = {
            "X-RapidAPI-Key": "dc2e72cb1cmsh271df14842a824bp190aaajsnf4720429b177",
            "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers).json()
        #print(response)
        name = response["title"]
        cover = response["cover_medium"]
        if(len(response["genres"]["data"]) > 0):
            genre = response["genres"]["data"][0]["name"]
        else:
            genre = "NONE"
        nb_tracks = response["nb_tracks"]
        duration = response["duration"]
        release_date = response["release_date"]
        record_type = response["record_type"]
        album = Album(deezer_id=deezerID,name=name,cover=cover,genre=genre,nb_tracks=nb_tracks,duration=duration,release_date=release_date,record_type=record_type,saved=saved)
        album.save()
        if not Artist.objects.filter(deezer_id = response["artist"]["id"]).exists():
            addArtistEntry(response["artist"]["id"],False)
        album.artist.add(Artist.objects.get(deezer_id = response["artist"]["id"]))

def addSongEntry(deezerID, saved):
    if not Song.objects.filter(deezer_id=deezerID).exists():
        url = "https://deezerdevs-deezer.p.rapidapi.com/track/" + str(deezerID)
        headers = {
        "X-RapidAPI-Key": "dc2e72cb1cmsh271df14842a824bp190aaajsnf4720429b177",
        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers).json()
        print(response)
        name = response["title"]
        duration = response["duration"]
        preview = response["preview"]
        song = Song(deezer_id=deezerID,name=name,duration=duration,preview=preview,saved=saved)
        song.save()
        if not Artist.objects.filter(deezer_id = response["artist"]["id"]).exists():
            addArtistEntry(response["artist"]["id"],False)
        song.artist.add(Artist.objects.get(deezer_id = response["artist"]["id"]))
        if not Album.objects.filter(deezer_id = response["album"]["id"]).exists():
            addAlbumEntry(response["album"]["id"],False)
        song.album.add(Album.objects.get(deezer_id = response["album"]["id"]))

def modifyArtistSaved(deezerID):
    if not Artist.objects.filter(deezer_id=deezerID).exists():
        addArtistEntry(deezerID, True)
    else:
        artist = Artist.objects.get(deezer_id=deezerID)
        artist.saved = not artist.saved
        artist.save()

def modifyAlbumSaved(deezerID):
    if not Album.objects.filter(deezer_id=deezerID).exists():
        addAlbumEntry(deezerID, True)
    else:
        album = Album.objects.get(deezer_id=deezerID)
        album.saved = not album.saved
        album.save()
        print(album.saved)

def modifySongSaved(deezerID):
    if not Song.objects.filter(deezer_id=deezerID).exists():
        addSongEntry(deezerID, True)
    else:
        song = Song.objects.get(deezer_id=deezerID)
        song.saved = not song.saved
        song.save()

def saveArtist(deezerID):
    if not Artist.objects.filter(deezer_id=deezerID).exists():
        addArtistEntry(deezerID, True)
    else:
        artist = Artist.objects.get(deezer_id=deezerID)
        artist.saved = True
        artist.save()

def saveAlbum(deezerID):
    if not Album.objects.filter(deezer_id=deezerID).exists():
        addAlbumEntry(deezerID, True)
        print("save is ONE")
    else:
        album = Album.objects.get(deezer_id=deezerID)
        print(album)
        album.saved = True
        album.save()
        print("save is TWO")

def saveSong(deezerID):
    if not Song.objects.filter(deezer_id=deezerID).exists():
        addSongEntry(deezerID, True)
    else:
        song = Song.objects.get(deezer_id=deezerID)
        song.saved = True
        song.save()

