from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('createEvent/', views.eventView, name = 'eventView'),
]
