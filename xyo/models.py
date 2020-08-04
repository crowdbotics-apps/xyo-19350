from django.conf import settings
from django.db import models


class Agency(models.Model):
    "Generated Model"
    name = models.TextField()
    identifier = models.TextField()


class Personnel(models.Model):
    "Generated Model"
    name = models.TextField()
    agency = models.ForeignKey(
        "xyo.Agency", on_delete=models.CASCADE, related_name="personnel_agency",
    )
    rank = models.TextField()
    phone = models.TextField()
    is_sten = models.BooleanField()
    sten_deployment = models.DateField()


# Create your models here.
