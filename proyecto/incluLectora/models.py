from django.db import models
from django.contrib.auth.models import User
import os


def upload_txt(instance, filename):
    # El archivo de texto será subido a MEDIA_ROOT/archivos_txt/<filename>
    return os.path.join('archivos_txt', filename)

def upload_audio(instance, filename):
    # El archivo de audio será subido a MEDIA_ROOT/archivos_audio/<filename>
    return os.path.join('archivos_audio', filename)




class MiModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
    # Agrega otros campos según sea necesario



class Archivo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    archivo_txt = models.FileField(upload_to=upload_txt)
    archivo_audio = models.FileField(upload_to=upload_audio)

    def __str__(self):
        return f"Archivo {self.id}: Usuario {self.usuario.id} - {self.usuario.username}, Archivo de Texto: {self.archivo_txt.name}, Archivo de Audio: {self.archivo_audio.name}"
