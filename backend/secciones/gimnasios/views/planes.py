from rest_framework import viewsets, permissions, status
from secciones.gimnasios.models.planes import Planes
from secciones.gimnasios.serializers.planes import PlanesModelSerializer
class PlanesViewSet(viewsets.ModelViewSet):

    queryset = Planes.objects.all()
    serializer_class = PlanesModelSerializer
    #filter_fields = ('gimnasio__pk',)