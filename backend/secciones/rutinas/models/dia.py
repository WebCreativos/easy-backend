from django.db import models as models
from secciones.rutinas.models.rutinas import Rutinas

class Dia(models.Model):

    nombre = models.CharField(max_length=100)
    repeticiones = models.IntegerField()
    dia = models.CharField(max_length=15)
    rutina = models.ForeignKey(Rutinas, on_delete=models.CASCADE)

