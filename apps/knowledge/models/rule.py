from django.db import models
from .disease import Disease
from .symptom import Symptom




class Rule(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.PROTECT, related_name="rules")
    symptom = models.ForeignKey(Symptom, on_delete=models.PROTECT, related_name="rules")
    cf_expert = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=["disease", "symptom"],
                name="unique_disease_symptom"
            )
        ]
