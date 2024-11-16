from django.urls import path

from . import views

app_name = "songs"

urlpatterns = [
  path("", views.SongList, name="list_view"),
  path("/song_search_results", views.search_results_view, name="search_results_view"),
  path("/<int:pk>",views.SongDetails, name="detail_view"),
]