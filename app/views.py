from django.shortcuts import render
from app.models import Team, Car

# Create your views here.
def index(request):
    features = Car.objects.order_by('-created_at').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_at')
    teams = Team.objects.all()
    context = {
        'teams':teams,
        'features':features,
        'cars':latest_cars,
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
    cars = Car.objects.all().order_by('-created_at')
    context = {
        'cars':cars,
    }
    return render(request, 'pages/cars.html', context)