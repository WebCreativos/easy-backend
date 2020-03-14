from secciones.usuarios.models.agenda import Agenda
from secciones.usuarios.serializers.usuarios import usuariosSerializer
from secciones.actividades.serializers.actividades import actividadesSerializer
from rest_framework import serializers
class agendaSerializer(serializers.ModelSerializer):
    user_data = usuariosSerializer(source="usuario", read_only=True)
    actividad_data = actividadesSerializer(source="actividad", read_only=True)
    class Meta:
        model = Agenda
        fields = (
            'pk', 
            'usuario', 
            'actividad', 
            'user_data',
            'actividad_data'
        )
