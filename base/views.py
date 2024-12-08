from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .job_scraper_utils import configure_webdriver, search_jobs, scrape_job_data, clean_data, send_email
from django.http import JsonResponse
import os
from dotenv import load_dotenv

load_dotenv()


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

def scrape_jobs_view(request):
    if request.method == "GET":
        job_position = request.GET.get('job_position', 'web developer')
        job_location = request.GET.get('job_location', 'remote')
        country = request.GET.get('country', 'https://www.indeed.com')
        date_posted = request.GET.get('date_posted', 20)

        try:
            driver = configure_webdriver()
            full_url = search_jobs(driver, country, job_position, job_location, date_posted)
            df = scrape_job_data(driver, country)

            if df.shape[0] == 1:
                return JsonResponse({'message': 'No results found for the given criteria.', 'url': full_url})

            cleaned_df = clean_data(df)
            csv_file = cleaned_df.to_csv(index=False)

            return JsonResponse({'message': 'Job scraping completed successfully!', 'data': cleaned_df.to_dict()})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        finally:
            driver.quit()

def job_scraper_home(request):
    return render(request, 'job_scraper/home.html')

def scrape_jobs(request):
    return render(request, 'job_scraper/results.html')

