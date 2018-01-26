from django.db import models

# Create your models here.
class Serie(models.Model):
    texto = models.CharField(max_length=10000)
