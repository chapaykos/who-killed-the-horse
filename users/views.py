from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views import View
from .forms import UserRegisterForm


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Założyłeś konto {username}! Teraz możesz się załadować')
            return redirect('users-login')
        else:
            form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'users/profile.html')
        else:
            return redirect('users-login')

# class LoginView(View):
#     def get(self, request):
#         form =
#         return render(request, 'users/register.html', {'form': form})