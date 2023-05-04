from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import eventForm
# Create your views here.
def eventView(request):
    if request.method == 'POST':
        form = eventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('your review has been taken')
        
        else:
            form = eventForm()

            