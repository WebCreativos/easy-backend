from django.urls import path, include
from rest_framework import routers
from secciones.gimnasios.views.gimnasios import gimnasiosViewSet
from secciones.gimnasios.views.planes import PlanesViewSet

router = routers.DefaultRouter()
router.register(r'gimnasios/planes', PlanesViewSet)
router.register(r'gimnasios', gimnasiosViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)


