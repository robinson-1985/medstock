from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrganizationScopedModel(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT
    )

    class Meta:
        abstract = True
