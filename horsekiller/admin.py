from django.contrib import admin
from .models import *

admin.site.register(Disease)
admin.site.register(Species)
admin.site.register(Diagnostics)
admin.site.register(Medicine)
admin.site.register(MedicalProcedure)
admin.site.register(MedicineOverdose)
admin.site.register(MedicineGroup)
admin.site.register(MedicineAlternative)
admin.site.register(MedicineContradictions)
admin.site.register(MedicineMarketNames)
admin.site.register(MedicineRecommendations)
admin.site.register(MedicineSideEffects)
