from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from horsekiller import views as horsekiller_views
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', horsekiller_views.HorseKillerIndexView.as_view(), name='horsekiller-home'),
    path('register/', users_views.RegisterView.as_view(), name='users-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('profile/', users_views.ProfileView.as_view(), name='users-profile'),
]
