import unittest
from django.urls import reverse
from django.test import Client
from .models import Usuarios
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_usuarios(**kwargs):
    defaults = {}
    defaults["email"] = "email"
    defaults["celular"] = "celular"
    defaults["nombre"] = "nombre"
    defaults["apellido"] = "apellido"
    defaults.update(**kwargs)
    return Usuarios.objects.create(**defaults)


class usuariosViewTest(unittest.TestCase):
    '''
    Tests for Usuarios
    '''
    def setUp(self):
        self.client = Client()

    def test_list_usuarios(self):
        url = reverse('usuarios_usuarios_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_usuarios(self):
        url = reverse('usuarios_usuarios_create')
        data = {
            "email": "email",
            "celular": "celular",
            "nombre": "nombre",
            "apellido": "apellido",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_usuarios(self):
        Usuarios = create_usuarios()
        url = reverse('usuarios_usuarios_detail', args=[Usuarios.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_usuarios(self):
        Usuarios = create_usuarios()
        data = {
            "email": "email",
            "celular": "celular",
            "nombre": "nombre",
            "apellido": "apellido",
        }
        url = reverse('usuarios_usuarios_update', args=[Usuarios.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


