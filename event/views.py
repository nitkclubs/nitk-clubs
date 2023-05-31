from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import eventForm
from .models import Event

# Create your views here.
def eventView(request):
    if request.method == 'POST':
        eventName = request.POST.get("eventName")
        eventDescription = request.POST.get("eventDescription")
        venue = request.POST.get("venue")
        datetime = request.POST.get("datetime")
        eventImg = request.FILES.get("eventImg")

        eventData = Event(eventName = eventName, eventDescription = eventDescription, venue = venue, datetime = datetime, eventImg = eventImg)

        form = eventForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            eventData.save()
            messages.success(request, 'Event created successfully.')
            return redirect('createEvent')
        
        else:
            messages.error(request, 'Event not created .')
            form = eventForm()
    return render(request, 'event/event.html')
            

def eventsBoard(request):
    events = Event.objects.all()
    return render(request, 'event/eventBoard.html', {'event' : events})