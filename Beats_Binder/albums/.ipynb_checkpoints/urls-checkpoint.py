from django.urls import path

from . import views

app_name = "album"

urlpatterns = [
	path("", views.home, name="home_view")
#   path("<int:album_id>", views.list_view, name="list_view"),
]