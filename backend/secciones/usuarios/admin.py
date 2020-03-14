from django.contrib import admin
from django import forms
from .models import Usuarios

class usuariosAdminForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = '__all__'


class usuariosAdmin(admin.ModelAdmin):
    form = usuariosAdminForm
    list_display = ['email', 'celular', 'nombre', 'apellido']
    readonly_fields = ['email', 'celular', 'nombre', 'apellido']

admin.site.register(Usuarios, usuariosAdmin)


