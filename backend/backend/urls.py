"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import  static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    url('/', include(('secciones.usuarios.urls','usuarios'), namespace='usuarios')),
    url('/', include(('secciones.gimnasios.urls','gimnasios'), namespace='gimnasios')),
    url('/', include(('secciones.rutinas.urls','rutinas'), namespace='rutinas')),
    url('/', include(('secciones.dietas.urls','rutinas'), namespace='dietas')),
    url('/', include(('secciones.eventos.urls','eventos'), namespace='eventos')),
    url('/', include(('secciones.actividades.urls','actividades'), namespace='actividades')),
    url(r'^admin/', admin.site.urls),
    url('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('login/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
