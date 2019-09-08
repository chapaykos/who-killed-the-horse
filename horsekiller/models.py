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
    predisposition = models.CharField(max_length=256)
    remarks_comments = models.TextField()
    survivability = models.CharField(max_length=256)
    diagnostics = models.ForeignKey("Diagnostics", on_delete=models.DO_NOTHING, blank=True, null=True)
    medical_procedure = models.ForeignKey('MedicalProcedure', on_delete=models.DO_NOTHING, blank=True, null=True)
    process = models.ForeignKey('DiseaseProcess', on_delete=models.DO_NOTHING, blank=True, null=True)  # TODO Czemu Alex chce osobną tablicę?
    disease_type = models.CharField(max_length=256)  # TODO Czemu Alex chce osobną tablicę?
    species = models.ForeignKey('Species', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.name_pl} - {self.name_en} - {self.name_lat}"

class Diagnostics(CommonInfo):
    interview = models.ForeignKey('Interview', on_delete=models.DO_NOTHING, blank=True, null=True)
    interview_text = models.TextField()
    changes_during_research = models.ForeignKey('ChangesDuringResearch', on_delete=models.DO_NOTHING, blank=True,
                                                null=True)
    behaviour = models.ForeignKey('Behaviour', on_delete=models.DO_NOTHING, blank=True, null=True)
    behaviour_text = models.TextField()
    incident_photos = models.ForeignKey('DiagnosticsPhotos', on_delete=models.DO_NOTHING, blank=True, null=True)
    # differential_diagnosis = models.ForeignKey('Disease', on_delete=models.DO_NOTHING) #TODO Odwrócona relacja, co robić?
    additional_check_up = models.ForeignKey('AdditionalCheckUp', on_delete=models.DO_NOTHING, blank=True, null=True)


class DiagnosticsPhotos(CommonInfo):
    incident_photos = models.ImageField(upload_to='incident_photos')


class Interview(CommonInfo):
    interview = models.CharField(max_length=256)


class Behaviour(CommonInfo):
    behaviour = models.CharField(max_length=256)


class MedicalProcedure(CommonInfo):
    immediate_action = models.CharField(max_length=256)
    essential_procedures = models.CharField(max_length=256)
    other_procedures_priority = models.CharField(max_length=256)
    owner_recommendations = models.CharField(max_length=256)
    treatment = models.ForeignKey('Treatment', on_delete=models.DO_NOTHING, blank=True, null=True)
    medicine = models.ForeignKey('Medicine', on_delete=models.DO_NOTHING, blank=True, null=True)


class DiseaseProcess(CommonInfo):
    disease_process = models.CharField(choices=DISEASE_PROCESS, max_length=256)


class Species(CommonInfo):
    species = models.CharField(choices=SPECIES, max_length=256)
    race = models.ForeignKey('Race', on_delete=models.DO_NOTHING, blank=True, null=True)


class Race(CommonInfo):
    race = models.CharField(max_length=256)


class ChangesDuringResearch(CommonInfo):
    system = models.ForeignKey('CDRSystem', on_delete=models.DO_NOTHING)
    detection_method = models.ForeignKey('CDRDetectionMethod', on_delete=models.DO_NOTHING)
    detection_method_text = models.TextField()


class CDRSystem(CommonInfo):
    system = models.CharField(max_length=256)


class CDRDetectionMethod(CommonInfo):
    detection_method = models.CharField(max_length=256)


class AdditionalCheckUp(CommonInfo):
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


class Treatment(CommonInfo):
    name = models.CharField(max_length=256)
    medicine_anesthetic = models.ForeignKey('Medicine', on_delete=models.DO_NOTHING, blank=True, null=True)
    notices = models.TextField()
    off_treatment_procedures = models.TextField()


class Medicine(CommonInfo):
    medicine_name = models.CharField(max_length=256, null=True)
    medicine_group = models.ManyToManyField('MedicineGroup', blank=True, null=True)
    recommendations = models.ManyToManyField('MedicineRecommendations', blank=True, null=True)
    contradictions = models.ManyToManyField('MedicineContradictions', blank=True, null=True)
    side_effects = models.ManyToManyField('MedicineSideEffects', blank=True, null=True)
    overdose = models.ManyToManyField('MedicineOverdose', blank=True, null=True)
    alternative = models.ManyToManyField('MedicineAlternative', blank=True, null=True)
    market_names = models.ManyToManyField('MedicineMarketNames', blank=True, null=True)
    market_names_text = models.TextField(blank=True)
    alternative_text = models.TextField(blank=True)
    doses = models.CharField(max_length=256, blank=True)
    medicine_application = models.CharField(max_length=256, blank=True)
    objects = PostManager()

    def get_absolute_url(self):
        return reverse('detail_medicine', kwargs={'pk': self.pk})

    def __str__(self):
        return self.medicine_name


class MedicineGroup(CommonInfo):
    medicine_group = models.CharField(max_length=256)

    def __str__(self):
        return self.medicine_group


class MedicineRecommendations(CommonInfo):
    recommendations = models.CharField(max_length=256)

    def __str__(self):
        return self.recommendations


class MedicineContradictions(CommonInfo):
    contradictions = models.CharField(max_length=256)

    def __str__(self):
        return self.contradictions


class MedicineSideEffects(CommonInfo):
    side_effects = models.CharField(max_length=256)

    def __str__(self):
        return self.side_effects


class MedicineOverdose(CommonInfo):
    overdose = models.CharField(max_length=256)

    def __str__(self):
        return self.overdose


class MedicineAlternative(CommonInfo):
    alternative = models.CharField(max_length=256)
    objects = PostManager()

    def __str__(self):
        return self.alternative


class MedicineMarketNames(CommonInfo):
    market_names = models.CharField(max_length=256)
    objects = PostManager()

    def __str__(self):
        return self.market_names
