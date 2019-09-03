from django.shortcuts import render
from django.core import paginator
from .models import *
from django.views import View
from .forms import AddDiseaseForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm


class HorseKillerIndexView(View):
    def get(self, request):
        form = AddDiseaseForm
        return render(request, 'horsekiller/index.html', {'form': form})
    def post(self, request):
        form = AddDiseaseForm(request.POST)