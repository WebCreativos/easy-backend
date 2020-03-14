from django.db import models as models
from secciones.usuarios.models.usuarios import Usuarios
from secciones.gimnasios.models.gimnasios import Gimnasios
from secciones.gimnasios.models.planes import Planes

class infoCliente(models.Model):

    # Fields
    opciones_sexos = [
        ("F","Femenino"),
        ("M","Masculino")
    ]
    opciones_figuras = [
        ("Reloj de arena","Reloj de arena"),
    ]


    fecha_pago = models.DateField(auto_now_add=False)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    gym_socio = models.ForeignKey(Gimnasios, on_delete=models.CASCADE)
    plan = models.ForeignKey(Planes, on_delete=models.CASCADE)
    sexo = models.CharField(choices=opciones_sexos, max_length=50, default="M")
    edad = models.IntegerField(default=0)
    altura = models.FloatField(default=0)
    peso = models.FloatField(default=0)
    pecho = models.IntegerField(default=0)
    cintura = models.IntegerField(default=0)
    piernas = models.IntegerField(default=0)
    tipo_de_figura = models.CharField(choices=opciones_figuras, max_length=50, default="Reloj de arena")
    puntos = models.IntegerField(default=0)