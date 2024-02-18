from django.contrib import admin
from .models import Archivo

class ArchivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'archivo_txt', 'archivo_audio')  # Lista de campos para mostrar en la vista de lista

admin.site.register(Archivo, ArchivoAdmin)