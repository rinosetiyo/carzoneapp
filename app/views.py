from django.shortcuts import render
from app.models import Team, Car

# Create your views here.
def index(request):
    features = Car.objects.order_by('-created_at').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_at')
    teams = Team.objects.all()
    model_search = Car.objects.values_list('model', flat=True).distinct()
    context = {
        'teams':teams,
        'features':features,
        'cars':latest_cars,
        'model_search':model_search,
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

def car_detail(request, slug):
    car = Car.objects.get(slug=slug)
    context = {
        'car':car,
    }
    return render(request, 'pages/car_detail.html', context)

def search(request):
    cars = Car.objects.order_by('-created_at')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = Car.objects.filter(title__icontains=keyword)

    if 'model' in request.GET:
        keyword = request.GET['model']
        if keyword:
            cars = Car.objects.filter(model__iexact=keyword)

    context = {
        'cars':cars,
    }
    return render(request, 'pages/search.html', context)