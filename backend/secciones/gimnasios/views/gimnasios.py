from secciones.gimnasios.models.gimnasios import Gimnasios
from secciones.gimnasios.serializers.gimnasios import gimnasiosSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

class gimnasiosViewSet(viewsets.ModelViewSet):
    """ViewSet for the Usuarios class"""

    queryset = Gimnasios.objects.all()
    serializer_class = gimnasiosSerializer
    #permission_classes = [permissions.IsAuthenticated]

