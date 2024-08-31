from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.
def fome(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    path('', views.home, name='home')