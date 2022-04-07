from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def workshops(request):
    return render(request, 'main/workshops.html')

def info(request):
    return render(request, 'main/info.html')

def projects(request):
    return render(request, 'main/projects.html')
