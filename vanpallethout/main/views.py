from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, you're at the index!")

def contact(request):
    return HttpResponse("Hello, you're at the contact page!")

def workshops(request):
    return HttpResponse("Hello, you're at the workshops page!")

def info(request):
    return HttpResponse("Hellow, you're at the infomation page!")

def projects(request):
    return HttpResponse("Hellow, you're at the projects page!")
