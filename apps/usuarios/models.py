from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.core.models import Organization

class User(AbstractUser):
    organization = models.ForeignKey(
        Organization, 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True
    )
