from django.urls import path, include
from rest_framework import routers
from secciones.eventos.views.eventos import eventosViewSet

router = routers.DefaultRouter()
router.register(r'eventos', eventosViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)


