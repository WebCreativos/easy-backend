from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from secciones.api.managers.managers import UserManager
objects = UserManager()
class Usuarios(AbstractUser):

    username = models.CharField(
        'ci',
        max_length=8,
        unique = True,
    )
    is_admin = models.BooleanField(
        'is_admin',
        default = False
    )
    is_active = models.BooleanField(
        'is_admin',
        default = True
    )

    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.ci
