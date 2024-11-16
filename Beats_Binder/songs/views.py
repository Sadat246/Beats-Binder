from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Song
from .song_search_form import SongSearchForm
import requests
from home.views import saveSong, modifySongSaved

# Create your views here.
	
def search_results_view(request):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(self, **kwargs)
        context = super().get_context_data(**kwargs)
        context["song_search_form"] = SongSearchForm
        return context
    if request.method == "GET":
        form = SongSearchForm(request.GET)
        if form.is_valid():
            search_input = form.cleaned_data["Search"]
            search_result = searchAPI(search_input)
            return render(request, "songs/song_search_results.html", context={"search_result": search_result["data"],
                                                                         "search_input": search_input,
                                                                          "song_search_form": form})
    if request.method == 'POST':
       saveSong(list(request.POST.keys())[1])
    else: 
        form = SongSearchForm()
    return render(request, "songs/song_search_results.html", 
            context={'song_search_form': SongSearchForm})
    
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

def SongList(request):
	object_list = Song.objects.all()
	#print(list(request.POST.keys())[1])
	if request.method == 'POST':
		modifySongSaved(list(request.POST.keys())[1])
	return render(request, "songs/song_list.html", context={"object_list": object_list,  "song_search_form": SongSearchForm})

def SongDetails(request, pk):
	song = Song.objects.get(pk=pk)
	return render(request, "songs/song_detail.html", context={"song": song,  "song_search_form": SongSearchForm})