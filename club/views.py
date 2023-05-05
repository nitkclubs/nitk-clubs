from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import clubForm
from .models import Club
# Create your views here.
def clubView(request):
    if request.method == 'POST':
        clubId = request.POST.get("clubId")
        clubName = request.POST.get("clubName")
        clubHeadRollno = request.POST.get("clubHeadRollno")
        clubDescription = request.POST.get("clubDescription")

        clubdata = Club(clubId, clubName = clubName, clubHead = clubHeadRollno, clubDescription = clubDescription)
        form = clubForm(request.POST)
        if form.is_valid():
            clubdata.save()
            form.save()
            return HttpResponse('Your review has been taken')
  
        else:
            form = clubForm()
            context = {
                'form':form,
            }
    return render(request, 'club/createClub.html')