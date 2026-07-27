from django.db import models

from apps.users.models import User
from apps.knowledge.models.disease import Disease
from apps.knowledge.models.recommendation import Recommendation


class Diagnosis(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="diagnoses",
    )

    result_disease = models.ForeignKey(
        Disease,
        on_delete=models.PROTECT,
        related_name="diagnoses",
    )

    recommendation = models.ForeignKey(
        Recommendation,
        on_delete=models.PROTECT,
        related_name="diagnoses",
    )

    cf_result = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "diagnoses"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.result_disease.name}"