from django.db import models as models
from secciones.gimnasios.models.gimnasios import Gimnasios

class Eventos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    gimnasio = models.ForeignKey(Gimnasios, on_delete=models.CASCADE)


