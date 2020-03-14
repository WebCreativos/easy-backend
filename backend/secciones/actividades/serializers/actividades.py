from rest_framework import serializers
from secciones.actividades.models.actividades import Actividades

class actividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividades
        fields = (
            'nombre',
            'dia',
            'hora',
            'gimnasio',
            'duracion',
            'pk'
        )


