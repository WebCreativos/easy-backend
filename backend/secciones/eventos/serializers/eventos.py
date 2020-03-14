from rest_framework import serializers
from secciones.eventos.models.eventos import Eventos

class eventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = (
            'pk', 
            'nombre', 
            'descripcion', 
            'gimnasio', 
        )
