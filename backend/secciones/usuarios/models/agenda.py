from django.db import models as models
from secciones.usuarios.models.usuarios import Usuarios
from secciones.actividades.models.actividades import Actividades

class Agenda(models.Model):

    # Fields
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividades, on_delete=models.CASCADE)

