from django.urls import path, include
from rest_framework import routers
from secciones.actividades.views.actividades import actividadesViewSet

router = routers.DefaultRouter()
router.register(r'actividades', actividadesViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)


