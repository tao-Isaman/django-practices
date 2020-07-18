from django.db import models

# Create your models here.


class Maid(models.Model):
    name = models.CharField(max_length=300)
    profile_image = models.FileField()
    birtdate = models.DateField()
    description = models.TextField()
    certificate = models.TextField()
    salary = models.IntegerField()
