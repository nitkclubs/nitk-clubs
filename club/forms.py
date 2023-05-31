from django import forms
from .models import Club

class clubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ('clubName', 'clubDescription', 'clubHead', 'clubImg')

