from django import forms
from .models import Event

class eventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('eventId', 'eventName', 'eventDescription', 'venue',  'datetime', 'duration')

