from django.db import models as models
from secciones.dietas.models.dietas import Dietas
class Dia(models.Model):

    nombre = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100, default="")
    dia = models.CharField(max_length=15)
    dieta = models.ForeignKey(Dietas, on_delete=models.CASCADE)

