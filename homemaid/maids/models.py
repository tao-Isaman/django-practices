from django.db import models

from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Maid(TimeStampedModel):
    name = models.CharField(max_length=300)
    profile_image = models.FileField()
    birtdate = models.DateField()
    description = models.TextField()
    certificate = models.TextField()
    salary = models.IntegerField()
