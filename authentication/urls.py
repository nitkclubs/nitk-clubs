from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('', views.aboutUs, name = 'aboutUs'),
    path('signin/', views.userLogin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
]
