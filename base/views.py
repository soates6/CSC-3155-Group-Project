from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Joblisting


def landing(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate and create the user
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created successfully!')
            # Redirect to login page after successful registration
            return redirect('login')

    return render(request, 'register.html')

def search(request):
    return render(request, 'search.html')

def terms_service(request):
    return render(request, 'terms_service.html')

def main(request):
    return render(request, 'main.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()  
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')

def home_view(request):
    return render(request, 'home.html')

def job_list(request):
    jobs = Joblisting.objects.all()
    return render(request, 'search.html', {'jobs': jobs})

def profiles(request):
    return render(request, 'profiles.html')