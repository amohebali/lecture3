from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ("Hello, World.!")

def pejman(request):
    return HttpResponse ("Hello pejman!")

def greet(request,name):
    return HttpResponse(f"Hello {name.capitalize()}!")