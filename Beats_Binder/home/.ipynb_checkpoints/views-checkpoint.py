from django.shortcuts import render
import requests
import json
import os
from artists.models import Artist
from albums.models import Album
from songs.models import Song

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

# Create your views here.

# for i in top_artists:
#     print(i)

def home_view(request):
    return render(request, 'home/home.html', 
                  context={'top_artists': top_artists,
                          'top_albums': top_albums,
                          'top_tracks': top_tracks})

def search_results_vew(request):
    return render(request, 'home/search_results.html')
    
def searchAPI():
    return render

def addSongEntry:
    