from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from horsekiller import views as horsekiller_views
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', horsekiller_views.SearchView.as_view(), name='horsekiller-home'),
    path('register/', users_views.RegisterView.as_view(), name='users-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('profile/', users_views.ProfileView.as_view(), name='users-profile'),
    path('medicine/new/', horsekiller_views.AddMedicineView.as_view(), name='add_medicine'),
    path('medicines/', horsekiller_views.ListMedicineView.as_view(), name='list_medicine'),
    path('medicine/<pk>/', horsekiller_views.DetailMedicineView.as_view(), name='detail_medicine'),
    path('medicine/<pk>/update', horsekiller_views.UpdateMedicineView.as_view(), name='update_medicine'),
    path('medicine/<pk>/delete', horsekiller_views.DeleteMedicineView.as_view(), name='delete_medicine'),
    path('disease/new/', horsekiller_views.AddDiseaseView.as_view(), name='add_disease'),

]
