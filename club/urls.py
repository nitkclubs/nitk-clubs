from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('createClub/', views.clubView, name = 'createClub'),
    path('clubDashboard/', views.clubDashboardView, name = 'clubDashboard'),
]
