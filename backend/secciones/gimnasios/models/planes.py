from django.db import models
from secciones.gimnasios.models.gimnasios import Gimnasios
class Planes(models.Model):
    nombre = models.CharField(max_length=50)
    duracion_dias = models.IntegerField()
    precio = models.IntegerField()
    gimnasio = models.ForeignKey(Gimnasios, on_delete=models.CASCADE)
