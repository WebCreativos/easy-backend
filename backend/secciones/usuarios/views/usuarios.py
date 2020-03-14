from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import APIException

#models
from secciones.usuarios.models.usuarios import Usuarios
from secciones.usuarios.models.asistencias import Asistencias
from secciones.usuarios.models.agenda import Agenda
from secciones.usuarios.models.info_cliente import infoCliente
from secciones.retos.models.retos import Retos
from secciones.gimnasios.models.gimnasios import Gimnasios
#serializers
from secciones.usuarios.serializers.usuarios import usuariosSerializer
from secciones.usuarios.serializers.agenda import agendaSerializer
from secciones.usuarios.serializers.info_cliente import infoClienteSerializer
from secciones.usuarios.serializers.retos_usuario import retosUsuarioSerializer
from secciones.usuarios.serializers.asistencias import AsistenciasSerializer
from datetime import datetime, timedelta
class usuariosViewSet(viewsets.ModelViewSet):
    """ViewSet for the Usuarios class"""

    queryset = Usuarios.objects.all()
    serializer_class = usuariosSerializer
    permission_classes = [permissions.IsAuthenticated]



    def get_permissions(self):
        permisos = []
        if self.action in ['setReto','getAgenda','SaveAgenda']:
            permisos.append(permissions.IsAuthenticated)
        else:
            permisos.append(permissions.AllowAny)

        return [p() for p in permisos]

    def get_queryset(self):
        try:
            gimnasio = Gimnasios.objects.get(administrador = 5)
            print(gimnasio.pk) 
            usuarios = Usuarios.objects.filter(pk__in=infoCliente.objects.filter(gym_socio=gimnasio.pk).values("usuario_id"))
            return usuarios
        except Exception as e:
            print(e)
            return []

    
    @action(detail = False, methods = ['get'])
    def loggedInUser(self, request):
        user = {}
        user = usuariosSerializer(self.request.user).data
        if request.user.is_authenticated:
            if request.user.vendedor == True:
                try: 
                    tienda = Tiendas.objects.get(vendedor = request.user.pk)
                    tienda = tiendasSerializer(tienda).data
                    user['tienda'] = tienda
                except :
                    print("No hay tienda")


        return Response(user, status.HTTP_200_OK)

    @action(detail = False, methods = ['post'])
    def SaveAgenda(self, request):
        """
        if request.user.is_authenticated:
            data = request.data 
            data["usuario"] = request.user.pk
            serializer = agendaSerializer(data = data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
        """
        data = request.data  
        serializer = agendaSerializer(data = data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()

        return Response(status.HTTP_201_CREATED)
    @action(detail = True, methods = ['get'])    
    def getAgenda(self, request, pk = None):
        data = Agenda.objects.filter(usuario = pk)
        response = agendaSerializer(data,many=True).data
        return Response(response,status.HTTP_200_OK)

    def create(self, request):
        data = request.data 

        serializer = usuariosSerializer(data = data) 
        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            response = usuariosSerializer(user).data
        return Response(response,status.HTTP_200_OK)

    @action(detail = True, methods = ['post'])    
    def setReto(self, request):
        data = {}
        data["reto"] = request.data 
        data["usuario"] = request.user.pk
        serializer = retosUsuarioSerializer(data = data) 
        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            response = usuariosSerializer(user).data
        return Response(response,status.HTTP_200_OK)

    @action(detail = True, methods = ['get'])    
    def setAsistencia(self, request, pk = None):
        try:
            usuario = self.get_object()
            infoCliente = infoCliente.objects.get(user = pk)
            diasPlan = infoCliente.plan.duracion_dias 
            fechaPago = infoCliente.fecha_pago + timedelta(days=diasPlan) 
            today = datetime.now() 
            if  today > fechaPago:
                raise APIException("Fecha impaga")
            infoAdicional
            data = {
                "usuario":pk
            }
            serializer = AsistenciasSerializer(data = data)
            if serializer.is_valid(raise_exception = True):
                    serializer.save()
            return Response(status.HTTP_200_OK)       
        except Exception as e:
            return Response("{}".format(e), status.HTTP_400_BAD_REQUEST)



    @action(detail = True, methods = ['get'])    
    def getAsistencia(self, request, pk = None):
        asistencias = Asistencias.objects.filter(usuario = pk)
        response = AsistenciasSerializer(asistencias, many = True).data
        return Response(response, status.HTTP_200_OK)
