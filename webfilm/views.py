from django.shortcuts import render, redirect, reverse
from webfilm.models import Films, Acteurs, Roles
from webfilm.api import get_movie
import requests


def index(request):
    films = Films.objects.all()
    return render(request, 'webfilm/index.html', {'liste_de_films': films})

def research(request):
    if request.method == 'GET':
        research = request.GET.get('research', None)
        movies = get_movie(research)
        myrequest = request
        film = Films.objects.filter(titre__icontains=research)
        acteur = Acteurs.objects.filter(nom__icontains=research)
        role = Roles.objects.filter(role__icontains=research)
        return render(request, 'webfilm/research.html', locals())

def specific_role(request, id):
    role = Roles.objects.get(id=id)
    return render(request, 'webfilm/role.html', {'role':role})
    
def specific_actor(request, id):
    actor = Acteurs.objects.get(id=id)
    role = Roles.objects.filter(acteur_id=id)
    return render(request, 'webfilm/actor.html', locals())

def specific_movie(request, id):
    movie = Films.objects.get(id=id)
    role = Roles.objects.filter(film_id=id)
    return render(request, 'webfilm/movie.html', locals())