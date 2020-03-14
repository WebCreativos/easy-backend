from secciones.rutinas.models.rutinas import Rutinas
from secciones.rutinas.models.dia import Dia
from secciones.rutinas.serializers.rutinas import rutinasSerializer
from secciones.rutinas.serializers.dia import diaSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

class rutinasViewSet(viewsets.ModelViewSet):
    """ViewSet for the Usuarios class"""

    queryset = Rutinas.objects.all()
    serializer_class = rutinasSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        data = request.data
        rutinas = data.pop("rutinas")
        data["nombre_rutina"] = "prueba"
        _rutinaSerializer = rutinasSerializer(data = data)
        if _rutinaSerializer.is_valid(raise_exception = True):
            rutina =_rutinaSerializer.save()
            for dia, valores in rutinas.items():
                for valor in valores:
                    valor["rutina"] = rutina.pk
                    valor["dia"] = dia
                    _diaSerializer = diaSerializer(data = valor)
                    if _diaSerializer.is_valid(raise_exception = True):
                        _diaSerializer.save()
        return Response({})

    def update(self, request, pk=None):
        data = request.data
        instance = self.get_object()
        rutinas = data.pop("rutinas")
        data["nombre_rutina"] = "prueba"
        _rutinaSerializer = rutinasSerializer(instance, data = data)
        if _rutinaSerializer.is_valid(raise_exception = True):
            rutina =_rutinaSerializer.save()
            print("aca")
            Dia.objects.filter(rutina = rutina.pk).delete()
            for dia, valores in rutinas.items():
                for valor in valores:
                    valor["rutina"] = rutina.pk
                    valor["dia"] = dia
                    _diaSerializer = diaSerializer(data = valor)
                    if _diaSerializer.is_valid(raise_exception = True):
                        _diaSerializer.save()
        return Response({})
