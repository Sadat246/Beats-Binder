from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Artist
from .artist_search_form import ArtistSearchForm
from home.views import saveArtist, modifyArtistSaved
import requests

# Create your views here.

class ArtistListView(ListView):
    model = Artist
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist_search_form'] = ArtistSearchForm
        return context

# class ArtistDetailView(DetailView):
# 	model = Artist
	
def search_results_view(request):
    if request.method == "GET":
        form = ArtistSearchForm(request.GET)
        if form.is_valid():
            search_input = form.cleaned_data["Search"]
            search_result = searchAPI(search_input)
            return render(request, "artists/artist_search_results.html", context={"search_result": search_result["data"],
                                                                        	"search_input": search_input,
                                                                            "artist_search_form": form})
    if request.method == 'POST':
       saveArtist(list(request.POST.keys())[1])
    else: 
        form = ArtistSearchForm()
    return render(request, "artists/artist_search_results.html", 
            context={ "artist_search_form": ArtistSearchForm})
    
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

def ArtistList(request):
	object_list = Artist.objects.all()
	#print(list(request.POST.keys())[1])
	if request.method == 'POST':
		modifyArtistSaved(list(request.POST.keys())[1])
	return render(request, "artists/artist_list.html", context={"object_list": object_list,  "artist_search_form": ArtistSearchForm})

def ArtistDetails(request, pk):
	artist = Artist.objects.get(pk=pk)
	return render(request, "artists/artist_detail.html", context={"artist": artist,  "artist_search_form": ArtistSearchForm})
