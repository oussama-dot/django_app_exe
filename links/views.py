from django.shortcuts import render
from .models import Link

# Create your views here.

def links(request):
    links_get = Link.objects.all()
    context = {
        "links_get" : links_get
        
    }
    
    
    
    return   render(request,"links/link.html",context)