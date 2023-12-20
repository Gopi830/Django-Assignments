from django.urls import path
from .views import *
urlpatterns = [

    path('search_movie_name/',search_movie_name),
]
