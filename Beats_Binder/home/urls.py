from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
  path("", views.home_view, name="home_view"),
  path("search_results", views.search_results_view, name="search_results_view"),
]