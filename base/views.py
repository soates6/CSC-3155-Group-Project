from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def search(request):
    return render(request, 'search.html')

def terms_service(request):
    return render(request, 'terms_service.html')

def main(request):
    return render(request, 'main.html')