from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from horsekiller import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.HorseKillerIndexView.as_view(), name='horsekiller-home'),
]
