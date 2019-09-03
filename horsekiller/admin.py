from django.contrib import admin
from .models import *

admin.site.register(Disease)
admin.site.register(Species)
admin.site.register(Diagnostics)
admin.site.register(Medicine)
admin.site.register(MedicalProcedure)
