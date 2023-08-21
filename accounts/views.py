from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now logged in. ')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')
        
    return render(request, 'accounts/login.html')

def register(request):
    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists !')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exists !')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, 
                    last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'you are now logged in, registered successfully. ')
                    user.save()
                    return redirect('dashboard')
        else:
            messages.error(request, 'password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/signup.html')
    
@login_required(login_url = 'login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    if request.POST:
        auth.logout(request)
        messages.success(request, 'you are successfully logged out')
        return redirect('index')
    return redirect('index')