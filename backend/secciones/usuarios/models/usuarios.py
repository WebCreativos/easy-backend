from django.urls import reverse
from django.db.models import CharField
from django.db.models import EmailField
from django.db.models import IntegerField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django.contrib.auth.models import AbstractUser


class Usuarios(AbstractUser):
    opciones_tipo = [
        ("Personal trainer","Personal trainer"),
        ("Cliente gimnasio","Cliente gimnasio"),
        ("Admin Gym","Admin Gym"),
        ("Cliente normal","Cliente normal"),
    ]
    username = models.EmailField(
        max_length=150,
        unique=True,
    )
    is_admin = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )
    celular = models.IntegerField()

    nombre = models.CharField(max_length=150)
    
    apellido = models.CharField(max_length=150)
    
    tipo = models.CharField(choices=opciones_tipo, max_length=150, default="Cliente normal")
    
    USERNAME_FIELD = 'username'


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('usuarios_usuarios_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('usuarios_usuarios_update', args=(self.pk,))
