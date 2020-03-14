from secciones.actividades.models.actividades import Actividades
from secciones.usuarios.models.agenda import Agenda
from secciones.rutinas.models.dia import Dia
from secciones.actividades.serializers.actividades import actividadesSerializer
from secciones.rutinas.serializers.dia import diaSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from secciones.usuarios.serializers.agenda import agendaSerializer

class actividadesViewSet(viewsets.ModelViewSet):
    """ViewSet for the Usuarios class"""

    queryset = Actividades.objects.all()
    serializer_class = actividadesSerializer
    #permission_classes = [permissions.IsAuthenticated]

    @action(detail = True, methods = ['get'])    
    def getUsuariosAgendados(self, request, pk = None):
        data = Agenda.objects.filter(actividad = pk)
        response = agendaSerializer(data,many=True).data
        return Response(response,status.HTTP_200_OK)
