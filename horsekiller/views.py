from django.shortcuts import render
from django.core import paginator
from .models import *
from django.views import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from itertools import chain


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


class UpdateMedicineView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Medicine
    fields = ['medicine_name', 'market_names', 'medicine_group', 'recommendations',
              'contradictions', 'side_effects', 'overdose',
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
    model = Medicine
    success_url = '/'

    def test_func(self):
        medicine = self.get_object()
        if self.request.user == medicine.author:
            return True
        else:
            return False


class AddMedicineView(LoginRequiredMixin, CreateView):
    model = Medicine
    fields = ['medicine_name', 'market_names', 'medicine_group', 'recommendations',
              'contradictions', 'side_effects', 'overdose',
              'alternative',
              'doses', 'medicine_application', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddDiseaseView(LoginRequiredMixin, CreateView):
    model = Disease
    form_class = DiseaseForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListDiseaseView(ListView):
    model = Disease
    fields = '__all__'


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
            blog_results = Medicine.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                blog_results,
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Medicine.objects.none()  # just an empty queryset as default
