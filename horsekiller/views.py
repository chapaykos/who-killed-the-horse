from django.shortcuts import render
from django.core import paginator
from .models import *
from django.views import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.views.generic import (CreateView, ListView,
                                  UpdateView, DeleteView, DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from itertools import chain


class HorseKillerIndexView(View):
    def get(self, request):
        return render(request, 'horsekiller/index.html')


# LEKI

class ListMedicineView(ListView):
    model = Drug
    context_object_name = 'medicine_list'
    fields = '__all__'


class DetailMedicineView(DetailView):
    model = Drug
    fields = '__all__'


class UpdateMedicineView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Drug
    fields = ['name', 'market_names', 'drug_class', 'recommendations',
              'contraindications', 'side_effects', 'overdose',
              'alternative',
              'doses', 'medicine_application', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        medicine = self.get_object()
        if self.request.user == medicine.author:
            return True
        else:
            return False


class DeleteMedicineView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Drug
    success_url = '/'

    def test_func(self):
        medicine = self.get_object()
        if self.request.user == medicine.author:
            return True
        else:
            return False


class AddMedicineView(LoginRequiredMixin, CreateView):
    model = Drug
    fields = ['name', 'market_names', 'drug_class', 'recommendations',
              'contraindications', 'side_effects', 'overdose',
              'alternative',
              'doses', 'medicine_application', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# CHOROBY

class AddDiseaseView(LoginRequiredMixin, CreateView):
    model = Disease
    form_class = DiseaseForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListDiseaseView(ListView):
    model = Disease
    fields = '__all__'


class DetailDiseaseView(DetailView):
    model = Disease
    fields = '__all__'


class UpdateDiseaseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Disease
    form_class = DiseaseForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        disease = self.get_object()
        if self.request.user == disease.author:
            return True
        else:
            return False


class DeleteDiseaseView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Disease
    success_url = '/'

    def test_func(self):
        disease = self.get_object()
        if self.request.user == disease.author:
            return True
        else:
            return False

# DIAGNOSTYKI

class AddDiagnosticView(LoginRequiredMixin, CreateView):
    model = Diagnosis
    form_class = DiagnosticForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListDiagnosticsView(ListView):
    model = Diagnosis
    fields = '__all__'


class DetailDiagnosticView(DetailView):
    model = Diagnosis
    fields = '__all__'


class UpdateDiagnosticView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Diagnosis
    form_class = DiagnosticForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        diagnostic = self.get_object()
        if self.request.user == diagnostic.author:
            return True
        else:
            return False


class DeleteDiagnosticView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Diagnosis
    success_url = '/'

    def test_func(self):
        diagnostic = self.get_object()
        if self.request.user == diagnostic.author:
            return True
        else:
            return False


# POSTĘPOWANIA MEDYCZNE

class AddMedicalProcedureView(LoginRequiredMixin, CreateView):
    model = MedicalProcedure
    form_class = MedicalProcedureForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListMedicalProcedureView(ListView):
    model = MedicalProcedure
    fields = '__all__'


class DetailMedicalProcedureView(DetailView):
    model = MedicalProcedure
    fields = '__all__'


class UpdateMedicalProcedureView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MedicalProcedure
    form_class = MedicalProcedureForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        medical_procedure = self.get_object()
        if self.request.user == medical_procedure.author:
            return True
        else:
            return False


class DeleteMedicalProcedureView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MedicalProcedure
    success_url = '/'

    def test_func(self):
        medical_procedure = self.get_object()
        if self.request.user == medical_procedure.author:
            return True
        else:
            return False

class SearchView(ListView):
    template_name = 'horsekiller/index.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            blog_results = Drug.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                blog_results,
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Drug.objects.none()  # just an empty queryset as default
