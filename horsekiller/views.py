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
    context_object_name = 'medicine_list'
    fields = '__all__'


class DetailMedicineView(DetailView):
    model = Medicine
    fields = '__all__'


class UpdateMedicineView(UpdateView):
    model = Medicine
    fields = '__all__'


class AddMedicineView(CreateView):
    model = Medicine
    fields = ['medicine_name', 'market_names', 'medicine_group', 'recommendations',
              'contradictions', 'side_effects', 'overdose',
              'alternative',
              'doses', 'medicine_application', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



