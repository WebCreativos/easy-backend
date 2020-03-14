from django.db import models as models
from secciones.usuarios.models.usuarios import Usuarios

class Gimnasios(models.Model):

    # Fields
    nombre = models.CharField(max_length=100)
    administrador = models.ForeignKey(Usuarios, on_delete=models.CASCADE)


