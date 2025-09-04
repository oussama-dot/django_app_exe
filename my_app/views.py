from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def about(request):
    return HttpResponse('about page')
def hello(request , first_name):
    return HttpResponse(f'hello {first_name}')
def add (request , num1 , num2):
    
    return HttpResponse(num1 + num2)