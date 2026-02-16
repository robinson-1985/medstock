from django.db import models
from apps.core.models import TimeStampedModel, OrganizationScopedModel

class Produto(TimeStampedModel, OrganizationScopedModel):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
