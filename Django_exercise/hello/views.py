from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def it3witch(request):
    return HttpResponse("Hello, it3witch!")

def roxy(request):
    return HttpResponse("Hello, roxy!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")