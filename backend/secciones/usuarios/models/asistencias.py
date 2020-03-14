from django.db import models
from secciones.usuarios.models.usuarios import Usuarios
class Asistencias(models.Model):

    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True, unique=True)
    asistio = models.BooleanField(default=True)