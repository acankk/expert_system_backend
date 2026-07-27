from django.db import models

from apps.knowledge.models.symptom import Symptom

from .diagnosis import Diagnosis


class DiagnosisDetail(models.Model):
    diagnosis = models.ForeignKey(
        Diagnosis,
        on_delete=models.CASCADE,
        related_name="details",
    )

    symptom = models.ForeignKey(
        Symptom,
        on_delete=models.PROTECT,
        related_name="diagnosis_details",
    )

    cf_user = models.DecimalField(
        max_digits=2,
        decimal_places=1,
    )

    cf_expert = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    cf_result = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    class Meta:
        db_table = "diagnosis_details"
        ordering = ["id"]

    def __str__(self):
        return f"{self.diagnosis.id} - {self.symptom.name}"