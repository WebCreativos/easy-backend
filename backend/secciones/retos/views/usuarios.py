from secciones.usuarios.models.usuarios import Usuarios
from secciones.usuarios.models.direccion import Direccion
from secciones.usuarios.serializers.usuarios import usuariosSerializer
from secciones.usuarios.serializers.direccion import direccionSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from secciones.tiendas.models.tiendas import Tiendas
from secciones.tiendas.serializers.tiendas import tiendasSerializer
from secciones.tiendas.serializers.ventas import ventasSerializer
from secciones.tiendas.models.ventas import Ventas

class usuariosViewSet(viewsets.ModelViewSet):
    """ViewSet for the Usuarios class"""

    queryset = Usuarios.objects.all()
    serializer_class = usuariosSerializer
    #permission_classes = [permissions.IsAuthenticated]


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

    @action(detail = False, methods = ['get'])
    def get_compras(self, request):
        ventas = Ventas.objects.filter(comprador = request.user.pk)
        data = ventasSerializer(ventas, many = True).data
        return Response(data) 

    def update(self, request, pk = None):
        usuario = request.user
        data = request.data
        envio = data["data_direccion"]
        serializerUsuario = usuariosSerializer(usuario, data=data, partial=True)
        
        if serializerUsuario.is_valid(raise_exception = True):
            serializerUsuario.save()

        if Direccion.objects.filter(usuario = usuario).exists():
            envio["usuario"] = usuario.pk
            direccion = Direccion.objects.get(usuario = usuario)
            serializerDireccion = direccionSerializer(direccion, data=envio) 
            if serializerDireccion.is_valid(raise_exception = True):
                serializerDireccion.save()
        else:
            envio["usuario"] = usuario.pk
            serializerDireccion = direccionSerializer(data=envio) 
            if serializerDireccion.is_valid(raise_exception = True):
                serializerDireccion.save()
        

        return Response(status.HTTP_200_OK)

