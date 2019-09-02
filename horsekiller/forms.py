from django import forms
from .models import Disease

class AddDiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = "__all__"