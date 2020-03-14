from secciones.usuarios.models.direccion import Direccion
from rest_framework import serializers


class direccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = (
            'departamento', 
            'ciudad', 
            'calle', 
            'numero',
            'pk',
            'usuario'
        )
