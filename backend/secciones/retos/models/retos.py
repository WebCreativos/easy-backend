from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import IntegerField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from secciones.gimnasios.models.gimnasios import Gimnasios

class Retos(models.Model):

    # Fields
    nombre = models.CharField(max_length=100)
    gimnasio = models.ForeignKey(Gimnasios, on_delete=models.CASCADE)


