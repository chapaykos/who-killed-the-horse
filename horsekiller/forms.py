from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        exclude = ['author']


class DiagnosticForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        exclude = ['author']

