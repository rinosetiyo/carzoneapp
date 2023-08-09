from django.shortcuts import render
from app.models import Team

# Create your views here.
def index(request):
    teams = Team.objects.all()
    context = {
        'teams':teams,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    teams = Team.objects.all()
    context = {
        'teams':teams,
    }
    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

def cars(request):
    return render(request, 'pages/cars.html')