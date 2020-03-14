from rest_framework import serializers
from secciones.gimnasios.models.planes import Planes
class PlanesModelSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Planes
        fields = (
            'nombre',
            'duracion_dias',
            'gimnasio',
            'precio',
            'pk' 
        )