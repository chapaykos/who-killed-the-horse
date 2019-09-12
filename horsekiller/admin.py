from django.contrib import admin
from .models import *

admin.site.register(Disease)
admin.site.register(Species)
admin.site.register(Diagnosis)
admin.site.register(Drug)
admin.site.register(MedicalProcedure)
admin.site.register(DrugOverdose)
admin.site.register(DrugClass)
admin.site.register(DrugAlternative)
admin.site.register(DrugContraindications)
admin.site.register(DrugMarketNames)
admin.site.register(DrugRecommendations)
admin.site.register(DrugSideEffects)
