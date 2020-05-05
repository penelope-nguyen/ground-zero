from django import forms

from .models import Flare

class FlareForm(forms.ModelForm):

    class Meta:
        model = Flare
        fields = ('title', 'description','location', 'priority', 'tags', 'latitude', 'longitude')
