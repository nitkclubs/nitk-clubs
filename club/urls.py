from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('createClub/', views.clubView, name = 'clubview'),
]
