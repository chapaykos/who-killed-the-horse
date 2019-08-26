from django.shortcuts import render
from django.core import paginator
from .models import *
from django.views import View

# Create your views here.

def HorseKillerView(request):
    return render(request, 'base.html')