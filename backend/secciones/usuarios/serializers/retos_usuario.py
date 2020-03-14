from rest_framework import serializers
from secciones.usuarios.models.retos_usuario import retosUsuario


class retosUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = retosUsuario
        fields = (
            'usuario',
            'reto',
        )
