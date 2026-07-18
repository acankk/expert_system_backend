from django.db import models

class Symptom(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.code:
            last_symptom = Symptom.objects.order_by("-id").first()

            if last_symptom is None:
                self.code = "G001"
            
            else:
                last_number = int(last_symptom.code[1:])
                next_number = last_number + 1
                self.code = f"G{next_number:03d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
    class Meta:
        db_table = "symptoms"
        ordering = ["-id"]
        