from secciones.dietas.models.dietas import Dietas
from secciones.dietas.models.dia import Dia
from secciones.dietas.serializers.dietas import dietasSerializer
from secciones.dietas.serializers.dia import diaSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

class dietasViewSet(viewsets.ModelViewSet):
    """ViewSet for the Usuarios class"""

    queryset = Dietas.objects.all()
    serializer_class = dietasSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        data = request.data
        dietas = data.pop("dietas")
        data["nombre_dieta"] = "prueba"
        _dietaSerializer = dietasSerializer(data = data)
        if _dietaSerializer.is_valid(raise_exception = True):
            dieta =_dietaSerializer.save()
            for dia, valores in dietas.items():
                for valor in valores:
                    valor["dieta"] = dieta.pk
                    valor["dia"] = dia
                    _diaSerializer = diaSerializer(data = valor)
                    if _diaSerializer.is_valid(raise_exception = True):
                        _diaSerializer.save()
        response = dietasSerializer(dieta).data
        return Response(response)

    def update(self, request, pk=None):
        data = request.data
        instance = self.get_object()
        dietas = data.pop("dietas")
        data["nombre_dieta"] = "prueba"
        _dietaSerializer = dietasSerializer(instance, data = data)
        if _dietaSerializer.is_valid(raise_exception = True):
            dieta =_dietaSerializer.save()
            Dia.objects.filter(dieta = dieta.pk).delete()
            for dia, valores in dietas.items():
                for valor in valores:
                    valor["dieta"] = dieta.pk
                    valor["dia"] = dia
                    _diaSerializer = diaSerializer(data = valor)
                    if _diaSerializer.is_valid(raise_exception = True):
                        _diaSerializer.save()
        response = dietasSerializer(dieta).data
        return Response(response)
