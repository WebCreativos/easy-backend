from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
#serializers
from secciones.eventos.serializers.eventos import eventosSerializer
#models
from secciones.eventos.models.eventos import Eventos

class eventosViewSet(viewsets.ModelViewSet):

    queryset = Eventos.objects.all()
    serializer_class = eventosSerializer
    #permission_classes = [permissions.IsAuthenticated]


