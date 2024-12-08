from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_scraper_home, name='job_scraper_home'),
    path('results/', views.scrape_jobs, name='scrape_jobs'),
]
