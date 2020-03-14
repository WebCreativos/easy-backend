from django.db import models as models
from secciones.gimnasios.models.gimnasios import Gimnasios

class Rutinas(models.Model):
    nombre_rutina = models.CharField(max_length=100)
    gimnasio = models.ForeignKey(Gimnasios, on_delete=models.CASCADE) 


