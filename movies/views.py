from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):
    return HttpResponse('hello from movies')
def index (request) :
    
    context = {
        "movies" : ["top gun", "what we do in the shadows", "gladiator", "22 jump street"]
    
        
    }
    
    return render(request, "movies/index.html",context)
def about (request) :
    return render(request, "movies/about.html",{})