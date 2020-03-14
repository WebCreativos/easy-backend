from django.urls import path, include
from rest_framework import routers
from secciones.usuarios.views.usuarios import usuariosViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', usuariosViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)


