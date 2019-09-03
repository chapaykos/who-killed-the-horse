from django import forms
from .models import Disease
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddDiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = "__all__"
