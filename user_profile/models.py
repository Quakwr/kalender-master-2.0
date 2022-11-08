from django.db import models

# Create your models here.

class Gasto(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    fecha = models.DateTimeField(auto_now=True)
    