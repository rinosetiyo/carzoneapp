from django.shortcuts import render, redirect, get_object_or_404
from app.models import Team, Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from app.models import Contact
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    features = Car.objects.order_by('-created_at').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_at')
    teams = Team.objects.all()
    
    # values list is for make list on dropdown without call object on template
    model_search = Car.objects.values_list('model', flat=True).distinct()
    location_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    context = {
        'teams':teams,
        'features':features,
        'cars':latest_cars,
        'model_search':model_search,
        'location_search':location_search,
        'year_search':year_search,
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

def cars(request):
    cars = Car.objects.order_by('-created_at')
    paginator = Paginator(cars, 6)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    location_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()

    context = {
        # 'cars':cars,
        'cars': paged_cars,
        'location_search':location_search,
        'year_search':year_search,
    }
    return render(request, 'pages/cars.html', context)

def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
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

    # iexact is for dropdown exactly choose
    if 'model' in request.GET:
        keyword = request.GET['model']
        if keyword:
            cars = Car.objects.filter(model__iexact=keyword)

    if 'city' in request.GET:
        keyword = request.GET['city']
        if keyword:
            cars = Car.objects.filter(city__iexact=keyword)

    if 'year' in request.GET:
        keyword = request.GET['year']
        if keyword:
            cars = Car.objects.filter(year__iexact=keyword)

    context = {
        'cars':cars,
    }
    return render(request, 'pages/search.html', context)

def contact(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = "You have a new message from carzone website regarding" + subject
        message_body = 'Name: '+ name + 'Email: '+ email + 'Phone: ' + phone + 'Message: ' + message

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email
        # send_mail(
        #     email_subject,
        #     message_body,
        #     admin_email,
        #     ['developer.rino@gmail.com'],
        #     fail_silently=False,
        # )

        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
    
    return render(request, 'pages/contact.html')

def inquiry(request):
    if request.POST:
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/' + car_id)
        
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email
        # send_mail(
        #     'New car inquiry',
        #     'You have a new inquiry for the car' + car_title + '. Please login to your admin panel for more info.',
        #     admin_email,
        #     ['developer.rino@gmail.com'],
        #     fail_silently=False,
        # )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/' + car_id)