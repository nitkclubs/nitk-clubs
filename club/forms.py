from django import forms
from .models import Club

class clubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ('clubId', 'clubName', 'clubDescription', 'clubHead')

