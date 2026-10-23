from django.shortcuts import render
from .models import Movie
import requests

def home(request):
    response = requests.get("https://omdbapi.com/?apikey=38b4b85b&s=Batman&type=movie")
    result_json = response.json()
    movies = result_json["Search"]
    context = {
        "movies": movies
    }
    return render(request, "index.html", context)

def home2(request):
    movies = Movie.object.all()
    return render(request, "home.html", {'movies': moveis})
    