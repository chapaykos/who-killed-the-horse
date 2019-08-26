from django.db import models

# Create your models here.

class Disease(models.Model):
    name_pl = models.CharField(max_length=128)
    name_lat = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    shorts = models.CharField(max_length=128)
    name_other = models.CharField(max_length=128)
    predisposition = models.CharField(max_length=128)
    notes_comments = models.TextField()

class Treatment(models.Model):
    immidiate = models.TextField()
    essential_treatment = models.TextField()
    owner_recommendations = models.TextField()
    procedure_priority = models.TextField()

class Medicine(models.Model):
    medicine_group = models.CharField(max_length=128)
    recommendations = models.TextField()
    doses = models.CharField(max_length=128)
    contradictions = models.TextField()
    side_effects = models.TextField()
    overdose = models.CharField(max_length=128)
    application = models.TextField()
    analogs = models.TextField()
    market_names = models.TextField()

class Species(models.Model):
    race = models.CharField(max_length=256)

class Diagnostic(models.Model):
    # wywiad, zachowania się, zmiany przy badaniu, badania dot., zdjęcia przypadków, diagnostyka różnicowa
    interview = models.TextField()
    behaviour = models.TextField()
    new_behaviour_changes = models.ForeignKey(BehaviourChanges)
    additional_examination = models.ForeignKey(AdditionalExamination)
    # photo_examples = models.  TODO how to add pics to database?
    differential_diagnosis = models.TextField()

class BehaviourChanges(models.Model):
    # w jakim układzie, jak stwierdzone
    which_system = models.TextField()
    verification = models.TextField()

class AdditionalExamination(models.Model):
    # zmiany krwi, zmiany moczu, zmiany anatopatomorfologiczne, kał, inne
    blood = models.TextField()
    urine = models.TextField()
    anat_pat = models.TextField()
    feces = models.TextField()
    other = models.TextField()

