from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('terms/', views.terms_service, name='terms'),
    path('main/', views.main, name='main'),


]
