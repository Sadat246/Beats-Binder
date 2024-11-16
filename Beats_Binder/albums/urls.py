from django.urls import path

from . import views

app_name = "albums"

urlpatterns = [
  path("",views.AlbumList ,name="list_view"),
  path("/<int:pk>",views.AlbumDetails ,name="detail_view"),
  path("/album_search_results", views.search_results_view, name="search_results_view"),
]