from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('terms/', views.terms_service, name='terms'),
    path('main/', views.main, name='main'),
]
