from rest_framework import serializers
from secciones.rutinas.models.rutinas import Rutinas
from secciones.rutinas.models.dia import Dia

class rutinasSerializer(serializers.ModelSerializer):
    rutinas = serializers.SerializerMethodField()
    class Meta:
        model = Rutinas
        fields = (
            'nombre_rutina',
            'pk',
            'rutinas',
            'gimnasio'
        )


    def get_rutinas(self, instance):
        dias = Dia.objects.filter(rutina= instance.pk).values()
        rutinas = dict()
        for dia in dias:

            if  dia["dia"] not in rutinas:
                rutinas[dia["dia"]] = list()

            rutinas[dia["dia"]].append(dia) 

        return rutinas

