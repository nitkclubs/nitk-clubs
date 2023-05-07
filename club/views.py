from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import clubForm
from .models import Club

# Create your views here.
def clubView(request):
    if request.method == 'POST':
        # clubId = request.POST.get("clubId")
        clubName = request.POST.get("clubName")
        clubHeadUsername = request.POST.get("clubHeadUsername")
        clubDescription = request.POST.get("clubDescription")

        clubdata = Club(clubName = clubName, clubHead = clubHeadUsername, clubDescription = clubDescription)
        form = clubForm(request.POST)
        clubdata.save()
        if form.is_valid:
            form.save()
            return HttpResponse('Your review has been taken')
  
        else:
            form = clubForm()
            context = {
                'form':form,
            }
    return render(request, 'club/createClub.html')