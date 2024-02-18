from gtts import gTTS
import os
from django.conf import settings

ruta_archivo = "archivo.txt"
text = ""
with open(ruta_archivo, "r", encoding='utf-8') as archivo:
    text = archivo.read()
    #print(text)

language = 'es-us'
speech = gTTS(text=text, lang=language, slow=False)
# Guardar el archivo de audio
speech.save("audio_GuardadoConError.mp3")

