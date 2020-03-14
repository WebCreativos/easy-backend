from django.db import models as models
from secciones.gimnasios.models.gimnasios import Gimnasios

class Actividades(models.Model):
    nombre = models.CharField(max_length=100)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    duracion = models.IntegerField()
    dia = models.DateField(auto_now=False, auto_now_add=False)
    gimnasio = models.ForeignKey(Gimnasios, on_delete=models.CASCADE) 

