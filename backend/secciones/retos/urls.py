from django.urls import path, include
from rest_framework import routers
from secciones.retos.views.retos import retosViewSet

router = routers.DefaultRouter()
router.register(r'retos', retosViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)


