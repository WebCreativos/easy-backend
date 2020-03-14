from secciones.usuarios.models.info_cliente import infoCliente
from rest_framework import serializers
from secciones.gimnasios.serializers.planes import PlanesModelSerializer


class infoClienteSerializer(serializers.ModelSerializer):
    info_plan = PlanesModelSerializer(source="plan",read_only=True)
    class Meta:
        model = infoCliente
        fields = (
            'fecha_pago',
            'usuario',
            'gym_socio',
            'plan',
            'info_plan'
        )
