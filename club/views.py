from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import clubForm
from .models import Club
from authentication.models import Student

# Create your views here.
def clubView(request):
    if request.method == 'POST':
        # clubId = request.POST.get("clubId")
        clubName = request.POST.get("clubName")
        clubHeadUsername = request.POST.get("clubHeadUsername")
        clubDescription = request.POST.get("clubDescription")
        clubImg = request.FILES.get('clubImg')
        clubdata = Club( clubName = clubName, clubHead = request.user, clubDescription = clubDescription, clubImg = clubImg)
        form = clubForm(request.POST)

        if request.user.is_superuser:
            clubdata.save()
            messages.success(request,'Your club is successfully created.')
            return redirect('createClub')
        else:
            messages.error(request, 'Only superusers can create a club.')
            return redirect('createClub')


    return render(request, 'club/createClub.html')

def createEvent(request):
    return render(request, 'event.html')


def clubDashboardView(request):
    students = Student.objects.all()
    clubs = Club.objects.all()
    return render(request,'club/clubDashboard.html', {'student': students, 'club': clubs})
