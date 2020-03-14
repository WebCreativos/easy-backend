from django.urls import path, include
from rest_framework import routers
from secciones.dietas.views.dietas import dietasViewSet

router = routers.DefaultRouter()
router.register(r'dietas', dietasViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)


