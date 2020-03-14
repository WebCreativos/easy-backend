from rest_framework import serializers
from secciones.dietas.models.dietas import Dietas
from secciones.dietas.models.dia import Dia

class dietasSerializer(serializers.ModelSerializer):
    dietas = serializers.SerializerMethodField()
    class Meta:
        model = Dietas
        fields = (
            'nombre_dieta',
            'pk',
            'dietas',
            'gimnasio'
        )


    def get_dietas(self, instance):
        dias = Dia.objects.filter(dieta = instance.pk).values()
        print(instance.pk)
        dietas = dict()
        for dia in dias:

            if  dia["dia"] not in dietas:
                dietas[dia["dia"]] = list()

            dietas[dia["dia"]].append(dia) 

        return dietas

