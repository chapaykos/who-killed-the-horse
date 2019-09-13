from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from horsekiller import views as horsekiller_views
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # UŻYTKOWNICY
    path('', horsekiller_views.SearchView.as_view(), name='horsekiller-home'),
    path('register/', users_views.RegisterView.as_view(), name='users-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('profile/', users_views.ProfileView.as_view(), name='users-profile'),
    # LEKI
    path('drug/new/', horsekiller_views.AddMedicineView.as_view(), name='add_medicine'),
    path('medicines/', horsekiller_views.ListMedicineView.as_view(), name='list_medicine'),
    path('drug/<pk>/', horsekiller_views.DetailMedicineView.as_view(), name='detail_medicine'),
    path('drug/<pk>/update', horsekiller_views.UpdateMedicineView.as_view(), name='update_medicine'),
    path('drug/<pk>/delete', horsekiller_views.DeleteMedicineView.as_view(), name='delete_medicine'),
    # CHOROBY
    path('disease/new/', horsekiller_views.AddDiseaseView.as_view(), name='add_disease'),
    path('diseases/', horsekiller_views.ListDiseaseView.as_view(), name='list_disease'),
    path('disease/<pk>/', horsekiller_views.DetailDiseaseView.as_view(), name='detail_disease'),
    path('disease/<pk>/update', horsekiller_views.UpdateDiseaseView.as_view(), name='update_disease'),
    path('disease/<pk>/delete', horsekiller_views.DeleteDiseaseView.as_view(), name='delete_disease'),
    # DIAGNOSTYKI
    path('diagnosis/', horsekiller_views.ListDiagnosticsView.as_view(), name='list_diagnostics'),
    path('diagnostic/new/', horsekiller_views.AddDiagnosticView.as_view(), name='add_diagnostic'),
    path('diagnostic/<pk>/', horsekiller_views.DetailDiagnosticView.as_view(), name='detail_diagnostic'),
    path('diagnostic/<pk>/update', horsekiller_views.UpdateDiagnosticView.as_view(), name='update_diagnostic'),
    path('diagnostic/<pk>/delete', horsekiller_views.DeleteDiagnosticView.as_view(), name='delete_diagnostic'),
    # POSTĘPOWANIA MEDYCZNE
    path('medical_procedure/', horsekiller_views.ListMedicalProcedureView.as_view(), name='list_medical_procedure'),
    path('medical_procedure/new/', horsekiller_views.AddMedicalProcedureView.as_view(), name='add_medical_procedure'),
    path('medical_procedure/<pk>/', horsekiller_views.DetailMedicalProcedureView.as_view(), name='detail_medical_procedure'),
    path('medical_procedure/<pk>/update', horsekiller_views.UpdateMedicalProcedureView.as_view(), name='update_medical_procedure'),
    path('medical_procedure/<pk>/delete', horsekiller_views.DeleteMedicalProcedureView.as_view(), name='delete_medical_procedure'),
    # ZABIEGI
    path('surgery/', horsekiller_views.ListSurgeryView.as_view(), name='list_surgery'),
    path('surgery/new/', horsekiller_views.AddSurgeryView.as_view(), name='add_surgery'),
    path('surgery/<pk>/', horsekiller_views.DetailSurgeryView.as_view(), name='detail_surgery'),
    path('surgery/<pk>/update', horsekiller_views.UpdateSurgeryView.as_view(), name='update_surgery'),
    path('surgery/<pk>/delete', horsekiller_views.DeleteSurgeryView.as_view(), name='delete_surgery'),
]
