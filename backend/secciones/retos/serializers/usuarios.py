from secciones.usuarios.models.usuarios import Usuarios
from secciones.usuarios.models.direccion import Direccion
from rest_framework import serializers
from secciones.usuarios.serializers.direccion import direccionSerializer

class usuariosSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = False)
    data_direccion = serializers.SerializerMethodField()
    class Meta:
        model = Usuarios
        fields = (
            'pk', 
            'username', 
            'celular', 
            'nombre', 
            'apellido', 
            'vendedor',
            'password',
            'is_admin',
            'data_direccion' 
        )
    def create(self, data):
        user = Usuarios()
        user.username = data["username"]
        user.is_admin = False
        user.is_active = True  
        user.nombre = data["nombre"]
        user.apellido = data["apellido"]
        user.vendedor = True if "vendedor" in data else False
        user.celular = data["celular"]
        user.set_password(data["password"])
        user.save()
        return user

    def get_data_direccion(self, instance):
        if Direccion.objects.filter(usuario = instance).exists():
            direccion = Direccion.objects.get(usuario = instance)
            data = direccionSerializer(direccion).data
            return data
        return {}
