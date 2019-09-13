from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile
from taggit.managers import TaggableManager
from django.urls import reverse
from django.db.models import Q

SPECIES = {

}

DISEASE_PROCESS = {

}


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(medicine_name__icontains=query) |
                         Q(doses__icontains=query) |
                         Q(medicine_application__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class CommonInfo(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True


class Disease(CommonInfo):
    name_pl = models.CharField(max_length=256)
    name_lat = models.CharField(max_length=256)
    name_en = models.CharField(max_length=256)
    name_other = models.CharField(max_length=256)
    abbreviations = models.CharField(max_length=256)
    predispositions = models.CharField(max_length=256)
    remarks_comments = models.TextField()
    survival_rate = models.CharField(max_length=256)
    diagnosis = models.ForeignKey("Diagnosis", on_delete=models.DO_NOTHING, blank=True, null=True)
    medical_procedure = models.ForeignKey('MedicalProcedure', on_delete=models.DO_NOTHING, blank=True, null=True)
    course_of_disease = models.CharField(choices=DISEASE_PROCESS, max_length=256)
    disease_form = models.CharField(max_length=256)
    species = models.ForeignKey('Species', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.name_pl} - {self.name_en} - {self.name_lat}"

    def get_absolute_url(self):
        return reverse('detail_disease', kwargs={'pk': self.pk})


class Diagnosis(CommonInfo):
    anamnesis = models.ForeignKey('Anamnesis', on_delete=models.DO_NOTHING, blank=True, null=True)
    anamnesis_text = models.TextField()
    changes_during_study = models.ForeignKey('ChangesDuringStudy', on_delete=models.DO_NOTHING, blank=True,
                                             null=True)
    behaviour = models.ForeignKey('Behaviour', on_delete=models.DO_NOTHING, blank=True, null=True)
    behaviour_text = models.TextField()
    case_photos = models.ForeignKey('DiagnosisPhotos', on_delete=models.DO_NOTHING, blank=True,
                                    null=True)
    # differential_diagnosis = models.ForeignKey('Disease', on_delete=models.DO_NOTHING) #TODO Odwrócona relacja, co robić?
    additional_tests = models.ForeignKey('AdditionalTests', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.anamnesis}"

    def get_absolute_url(self):
        return reverse('detail_diagnostic', kwargs={'pk': self.pk})


class DiagnosisPhotos(CommonInfo):
    incident_photos = models.ImageField(upload_to='case_photos')


class Anamnesis(CommonInfo):
    anamnesis = models.CharField(max_length=256)


class Behaviour(CommonInfo):
    behaviour = models.CharField(max_length=256)


class MedicalProcedure(CommonInfo):
    immediate_action = models.CharField(max_length=256, blank=True, null=True)
    essential_procedures = models.CharField(max_length=256, blank=True, null=True)
    other_procedures_priority = models.CharField(max_length=256, blank=True, null=True)
    owner_recommendations = models.CharField(max_length=256, blank=True, null=True)
    surgery = models.ForeignKey('Surgery', on_delete=models.DO_NOTHING, blank=True, null=True)
    drug = models.ForeignKey('Drug', on_delete=models.DO_NOTHING, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('detail_medical_procedure', kwargs={'pk': self.pk})


class Surgery(CommonInfo):
    name = models.CharField(max_length=256)
    drug_anasthesia = models.ForeignKey('Drug', on_delete=models.DO_NOTHING, blank=True, null=True)
    comments = models.TextField()
    off_treatment_procedures = models.TextField()

    def get_absolute_url(self):
        return reverse('detail_surgery', kwargs={'pk': self.pk})


class Species(CommonInfo):
    species = models.CharField(choices=SPECIES, max_length=256)
    race = models.ForeignKey('Race', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.species


class Race(CommonInfo):
    race = models.CharField(max_length=256)


class ChangesDuringStudy(CommonInfo):
    system = models.ForeignKey('CDRSystem', on_delete=models.DO_NOTHING)
    name = models.ForeignKey('CDSName', on_delete=models.DO_NOTHING)


class CDRSystem(CommonInfo):
    system = models.CharField(max_length=256)


class CDSName(CommonInfo):
    name = models.CharField(max_length=256)


class AdditionalTests(CommonInfo):
    blood_changes = models.ForeignKey('BloodChanges', on_delete=models.DO_NOTHING)
    urine_changes = models.ForeignKey('UrineChanges', on_delete=models.DO_NOTHING)
    feces = models.ForeignKey('Feces', on_delete=models.DO_NOTHING)
    anat_pat_mor_changes = models.ForeignKey('AnatPatMorChanges', on_delete=models.DO_NOTHING)
    other = models.TextField()


class BloodChanges(CommonInfo):
    blood_changes = models.CharField(max_length=256)


class UrineChanges(CommonInfo):
    urine_changes = models.CharField(max_length=256)


class Feces(CommonInfo):
    feces = models.CharField(max_length=256)


class AnatPatMorChanges(CommonInfo):
    anat_pat_mor_changes = models.CharField(max_length=256)


class Drug(CommonInfo):
    name = models.CharField(max_length=256, null=True)
    drug_class = models.ManyToManyField('DrugClass', blank=True, null=True)
    recommendations = models.ManyToManyField('DrugRecommendations', blank=True, null=True)
    contraindications = models.ManyToManyField('DrugContraindications', blank=True, null=True)
    side_effects = models.ManyToManyField('DrugSideEffects', blank=True, null=True)
    overdose = models.ManyToManyField('DrugOverdose', blank=True, null=True)
    alternative = models.ManyToManyField('DrugAlternative', blank=True, null=True)
    market_names = models.ManyToManyField('DrugMarketNames', blank=True, null=True)
    market_names_text = models.TextField(blank=True)
    alternative_text = models.TextField(blank=True)
    doses = models.CharField(max_length=256, blank=True)
    medicine_application = models.CharField(max_length=256, blank=True)
    objects = PostManager()

    def get_absolute_url(self):
        return reverse('detail_medicine', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class DrugClass(CommonInfo):
    drug_class = models.CharField(max_length=256)

    def __str__(self):
        return self.drug_class


class DrugRecommendations(CommonInfo):
    recommendations = models.CharField(max_length=256)

    def __str__(self):
        return self.recommendations


class DrugContraindications(CommonInfo):
    contraindications = models.CharField(max_length=256)

    def __str__(self):
        return self.contraindications


class DrugSideEffects(CommonInfo):
    side_effects = models.CharField(max_length=256)

    def __str__(self):
        return self.side_effects


class DrugOverdose(CommonInfo):
    overdose = models.CharField(max_length=256)

    def __str__(self):
        return self.overdose


class DrugAlternative(CommonInfo):
    alternative = models.CharField(max_length=256)
    objects = PostManager()

    def __str__(self):
        return self.alternative


class DrugMarketNames(CommonInfo):
    market_names = models.CharField(max_length=256)
    objects = PostManager()

    def __str__(self):
        return self.market_names
