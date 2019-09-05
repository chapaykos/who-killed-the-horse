from django.shortcuts import render
from django.core import paginator
from .models import *
from django.views import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


class HorseKillerIndexView(View):
    def get(self, request):
        return render(request, 'horsekiller/index.html')


class ListMedicineView(ListView):
    model = Medicine
    fields = '__all__'


class DetailMedicineView(DetailView):
    model = Medicine
    fields = '__all__'


class UpdateMedicineView(UpdateView):
    model = Medicine
    fields = '__all__'


class AddMedicineView(CreateView):
    model = Medicine
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



