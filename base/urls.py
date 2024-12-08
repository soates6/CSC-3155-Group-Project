from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    # Home and main pages
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),

    # User authentication
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Additional pages
    path('search/', views.search, name='search'),
    path('terms/', views.terms_service, name='terms'),

    # Job scraper
    path('scrape-jobs/', views.scrape_jobs_view, name='scrape_jobs'),
    path('', views.job_scraper_home, name='job_scraper_home'),
    path('results/', views.scrape_jobs, name='scrape_jobs'),
]

