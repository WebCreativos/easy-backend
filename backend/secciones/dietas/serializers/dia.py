from rest_framework import serializers
from secciones.dietas.models.dia import Dia

class diaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dia 
        fields = '__all__'
