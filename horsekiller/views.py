from django.shortcuts import render
from django.core import paginator
from .models import *
from django.views import View
from .forms import AddDiseaseForm

# Create your views here.

class HorseKillerIndexView(View):
    def get(self, request):
        form = AddDiseaseForm
        return render(request, 'horsekiller/index.html')