from django.db import models

# Create your models here.

class Maid(models.Model):
    name = models.CharField(max_length=300)
    birtdate = models.DateField()
    description = models.TextField()
    certificate = models.TextField()
    salary = models.IntegerField()
