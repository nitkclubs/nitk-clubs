from django import forms
from .models import Event

class eventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('eventName', 'eventDescription', 'venue',  'datetime', 'eventImg')

