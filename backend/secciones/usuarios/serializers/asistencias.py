from rest_framework import serializers
from secciones.usuarios.models.asistencias import Asistencias
class AsistenciasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asistencias
        fields = '__all__'