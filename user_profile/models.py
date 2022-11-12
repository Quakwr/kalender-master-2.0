from django.db import models

# Create your models here.

class Gasto(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    fecha = models.DateTimeField(auto_now=True)
    
class calendario(models.Model):
    titulo = models.CharField(max_length=100)
    hecho = models.BooleanField(default= False)
    crear = models.DateTimeField(auto_now_add = True)
    fecha = models.DateTimeField(auto_now_add = False, auto_now = False, blank = True, null = True)

    def __str__(self):
        return self.titulo
