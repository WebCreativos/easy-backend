from django.db import models as models
from secciones.retos.models.retos import Retos
from secciones.usuarios.models.usuarios import Usuarios

class retosUsuario(models.Model):

    # Fields
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    gimnasio = models.ForeignKey(Retos, on_delete=models.CASCADE)


