from django.core.exceptions import ValidationError
from django.db import models

from .disease import Disease


class Recommendation(models.Model):
    disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE,
        related_name="recommendations",
    )

    min_cf = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    max_cf = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    confidence = models.CharField(
        max_length=50,
    )

    recommendation = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        db_table = "recommendations"
        constraints = [
            models.UniqueConstraint(
                fields=["disease", "confidence"],
                name="unique_disease_confidence",
            )
        ]
        ordering = ["disease", "min_cf"]

    def clean(self):
        if self.min_cf < 0 or self.max_cf > 1:
            raise ValidationError(
                "Nilai CF harus berada pada rentang 0 sampai 1."
            )

        if self.min_cf >= self.max_cf:
            raise ValidationError(
                "Nilai min_cf harus lebih kecil dari max_cf."
            )

    def __str__(self):
        return f"{self.disease.name} - {self.confidence}"