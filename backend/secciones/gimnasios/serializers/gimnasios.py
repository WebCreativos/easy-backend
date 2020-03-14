from secciones.gimnasios.models.gimnasios import Gimnasios
from rest_framework import serializers


class gimnasiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gimnasios
        fields = '__all__'
