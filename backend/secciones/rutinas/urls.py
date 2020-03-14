from django.urls import path, include
from rest_framework import routers
from secciones.rutinas.views.rutinas import rutinasViewSet

router = routers.DefaultRouter()
router.register(r'rutinas', rutinasViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)


