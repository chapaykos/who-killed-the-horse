from django.db import models

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
    process = models.ForeignKey('DiseaseProcess', on_delete=models.DO_NOTHING) #TODO Czemu Alex chce osobną tablicę?
    disease_type = models.CharField(max_length=256) #TODO Czemu Alex chce osobną tablicę?
    species = models.ForeignKey('Species', on_delete=models.DO_NOTHING)

class Diagnostics(models.Model):
    # TODO interview = models.MultipleChoiceField - https://pypi.org/project/django-select-multiple-field/ or https://pypi.org/project/django-multiselectfield/
    interview_text = models.TextField()
    changes_during_research = models.ForeignKey("", on_delete=models.DO_NOTHING)
    # TODO behaviour = models.MultipleChoiceField
    behaviour_text = models.TextField()
    # TODO incident_photos = models.ImageField()
    # TODO differential_diagnosis = models.ChoiceField z tabeli Diseases
    additional_check-up = models.ForeignKey('AdditionalCheckUp', on_delete=models.DO_NOTHING)

class MedicalProcedure(models.Model):
    immediate_action = models.CharField(max_length=256)
    essential_procedures = models.CharField(max_length=256)
    other_procedures_priority = models.CharField(max_length=256)
    owner_recommendations = models.CharField(max_length=256)
    treatment = models.ForeignKey('Treatment', on_delete=models.DO_NOTHING)
    medicine = models.ForeignKey('Medicine', on_delete=models.DO_NOTHING)

class DiseaseProcess(models.Model):
    # disease_process = models.CharField(choices=) #TODO - dodać selekcję

class Species(models.Model):
    # species = models.CharField(choices=) #TODO - czy to dobry wybór?...
    # race = models.MultipleChoiceField #TODO - multiple choice

class ChangesDuringResearch(models.Model):
    # system = models.MultipleChoiceField TODO - multiple choice
    # detection_method = models.MultipleChoiceField TODO - multiple choice
    detection_method = models.TextField()

class AdditionalCheckUp(models.Model):
    # blood_changes = models.MultipleChoiceField TODO - multiple choice
    # urine_changes = models.MultipleChoiceField TODO - multiple choice
    # feces = models.MultipleChoiceField TODO - multiple choice
    # anat_pat_mor_changes = models.MultipleChoiceField TODO - multiple choice
    other = models.TextField()

class Treatment(models.Model):
    name = models.CharField(max_length=256)
    medicine_anesthetic = models.ForeignKey('Medicine')
    notices = models.TextField()
    off_treatment_procedures = models.TextField()

class Medicine(models.Model):
    # medicine_group = multiplechoice
    # recommendations = multiplechoice
    # contradictions = multiplechoice
    # side_effects = multiplechoice
    # overdose = multiplechoice
    # alternative = multiplechoice
    # market_names = multiplechoice
    market_names_text = models.TextField()
    alternative_text = models.TextField()
    doses = models.ForeignKey('Doses', on_delete=models.DO_NOTHING)
    application = models.ForeignKey('MedicineApplication', on_delete=models.DO_NOTHING)

class Doses(models.Model):
    dawka = models.CharField(max_length=256) #TODO A czemu tak? Nie można razem

class MedicineApplication(models.Model):
    medicine_application = models.CharField(max_length=256) #TODO A czemu tak? Nie można razem


