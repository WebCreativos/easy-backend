from secciones.usuarios.models.usuarios import Usuarios
from secciones.usuarios.models.info_cliente import infoCliente
from rest_framework import serializers
from secciones.usuarios.serializers.info_cliente import infoClienteSerializer
from datetime import datetime 
class usuariosSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = False)
    data_info_cliente = serializers.SerializerMethodField()
    info_cliente = serializers.JSONField(write_only= True)
    class Meta:
        model = Usuarios
        fields = (
            'pk', 
            'username', 
            'celular', 
            'nombre', 
            'apellido', 
            'password',
            'is_admin',
            'is_active',
            'info_cliente', 
            'data_info_cliente' 
        )
    def create(self, data):
        print(data)
        info_cliente = dict(data.pop("info_cliente"))
        data["is_admin"] = False
        data["is_admin_gym"] = False
        data["is_active"] = False
        try:
            user = Usuarios.objects.create(**data)
            info_cliente["usuario"] = user.pk
            info_cliente["gym_socio"] = 1
            serializer = infoClienteSerializer(data=info_cliente)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
        except Exception as e:
            print(e)
        return user


    def get_data_info_cliente(self, instance):
        try:
            info_cliente = infoCliente.objects.get(usuario = instance.pk)
            data = infoClienteSerializer(info_cliente).data
            return data 
        except Exception as e:
            return {}
    """
    def to_representation(self, instance):
        response = super(usuariosSerializer, self).to_representation(instance)
        if 'fecha' in instance.data_info_cliente: 
            response['data_info_cliente']["fecha"] = instance
        return response
    """