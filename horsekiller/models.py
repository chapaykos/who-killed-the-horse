from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

SPECIES = {

}

DISEASE_PROCESS = {

}


class Disease(models.Model):
    name_pl = models.CharField(max_length=256)
    name_lat = models.CharField(max_length=256)
    name_en = models.CharField(max_length=256)
    name_other = models.CharField(max_length=256)
    predisposition = models.CharField(max_length=256)
    remarks_comments = models.TextField()
    survivability = models.CharField(max_length=256)
    diagnostics = models.ForeignKey("Diagnostics", on_delete=models.DO_NOTHING)
    medical_procedure = models.ForeignKey('MedicalProcedure', on_delete=models.DO_NOTHING)
    process = models.ForeignKey('DiseaseProcess', on_delete=models.DO_NOTHING)  # TODO Czemu Alex chce osobną tablicę?
    disease_type = models.CharField(max_length=256)  # TODO Czemu Alex chce osobną tablicę?
    species = models.ForeignKey('Species', on_delete=models.DO_NOTHING)


class Diagnostics(models.Model):
    interview = models.ForeignKey('Interview', on_delete=models.DO_NOTHING)
    interview_text = models.TextField()
    changes_during_research = models.ForeignKey('ChangesDuringResearch', on_delete=models.DO_NOTHING)
    behaviour = models.ForeignKey('Behaviour', on_delete=models.DO_NOTHING)
    behaviour_text = models.TextField()
    # incident_photos = models.ImageField() #TODO jak załączać obrazki?
    # differential_diagnosis = models.ForeignKey('Disease', on_delete=models.DO_NOTHING) #TODO Odwrócona relacja, co robić?
    additional_check_up = models.ForeignKey('AdditionalCheckUp', on_delete=models.DO_NOTHING)


class Interview(models.Model):
    interview = models.CharField(max_length=256)


class Behaviour(models.Model):
    behaviour = models.CharField(max_length=256)


class MedicalProcedure(models.Model):
    immediate_action = models.CharField(max_length=256)
    essential_procedures = models.CharField(max_length=256)
    other_procedures_priority = models.CharField(max_length=256)
    owner_recommendations = models.CharField(max_length=256)
    treatment = models.ForeignKey('Treatment', on_delete=models.DO_NOTHING)
    medicine = models.ForeignKey('Medicine', on_delete=models.DO_NOTHING)


class DiseaseProcess(models.Model):
    disease_process = models.CharField(choices=DISEASE_PROCESS, max_length=256)


class Species(models.Model):
    species = models.CharField(choices=SPECIES, max_length=256)
    race = models.ForeignKey('Race', on_delete=models.DO_NOTHING)


class Race(models.Model):
    race = models.CharField(max_length=256)


class ChangesDuringResearch(models.Model):
    system = models.ForeignKey('CDRSystem', on_delete=models.DO_NOTHING)
    detection_method = models.ForeignKey('CDRDetectionMethod', on_delete=models.DO_NOTHING)
    detection_method_text = models.TextField()


class CDRSystem(models.Model):
    system = models.CharField(max_length=256)


class CDRDetectionMethod(models.Model):
    detection_method = models.CharField(max_length=256)


class AdditionalCheckUp(models.Model):
    blood_changes = models.ForeignKey('BloodChanges', on_delete=models.DO_NOTHING)
    urine_changes = models.ForeignKey('UrineChanges', on_delete=models.DO_NOTHING)
    feces = models.ForeignKey('Feces', on_delete=models.DO_NOTHING)
    anat_pat_mor_changes = models.ForeignKey('AnatPatMorChanges', on_delete=models.DO_NOTHING)
    other = models.TextField()


class BloodChanges(models.Model):
    blood_changes = models.CharField(max_length=256)


class UrineChanges(models.Model):
    urine_changes = models.CharField(max_length=256)


class Feces(models.Model):
    feces = models.CharField(max_length=256)


class AnatPatMorChanges(models.Model):
    anat_pat_mor_changes = models.CharField(max_length=256)


class Treatment(models.Model):
    name = models.CharField(max_length=256)
    medicine_anesthetic = models.ForeignKey('Medicine', on_delete=models.DO_NOTHING)
    notices = models.TextField()
    off_treatment_procedures = models.TextField()


class Medicine(models.Model):
    medicine_group = models.ForeignKey('MedicineGroup', on_delete=models.DO_NOTHING)
    recommendations = models.ForeignKey('MedicineRecommendations', on_delete=models.DO_NOTHING)
    contradictions = models.ForeignKey('MedicineContradictions', on_delete=models.DO_NOTHING)
    side_effects = models.ForeignKey('MedicineSideEffects', on_delete=models.DO_NOTHING)
    overdose = models.ForeignKey('MedicineOverdose', on_delete=models.DO_NOTHING)
    alternative = models.ForeignKey('MedicineAlternative', on_delete=models.DO_NOTHING)
    market_names = models.ForeignKey('MedicineMarketNames', on_delete=models.DO_NOTHING)
    market_names_text = models.TextField()
    alternative_text = models.TextField()
    doses = models.CharField(max_length=256)
    medicine_application = models.CharField(max_length=256)


class MedicineGroup(models.Model):
    medicine_group = models.CharField(max_length=256)


class MedicineRecommendations(models.Model):
    recommendations = models.CharField(max_length=256)


class MedicineContradictions(models.Model):
    contradictions = models.CharField(max_length=256)


class MedicineSideEffects(models.Model):
    side_effects = models.CharField(max_length=256)


class MedicineOverdose(models.Model):
    overdose = models.CharField(max_length=256)


class MedicineAlternative(models.Model):
    alternative = models.CharField(max_length=256)


class MedicineMarketNames(models.Model):
    market_names = models.CharField(max_length=256)
