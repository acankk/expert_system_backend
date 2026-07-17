from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="profile_picture")


    def __str__(self):
        return self.username

