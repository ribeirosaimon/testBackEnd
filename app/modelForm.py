from django import forms
from django.db.models import fields
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ["name","log","lat","timestamp", "visit"]