from django.shortcuts import render, redirect
from .models import Movie
import requests
from django.contrib.auth.models import User

def home(request):
    response = requests.get("https://omdbapi.com/?apikey=38b4b85b&s=Batman&type=movie")
    result_json = response.json()
    movies = result_json["Search"]
    context = {
        "movies": movies
    }
    return render(request, "index.html", context)

def home2(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {'movies': movies})

def create_user(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            request.POST["username"],
            request.POST["email"],
            request.POST["password"]
            )
        user.save()
        return redirect('login')
    return render(request, "register.html",
                  context={'action': 'Adicionar'})

def login_user(request):
    pass


