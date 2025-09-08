from django.contrib import admin
from django.urls import path
from .views import main , details
urlpatterns = [
    path('', main, name = 'main'),
    path('job/<int:pk>',details ,name = "details")
]