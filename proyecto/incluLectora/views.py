import os
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from django.http import JsonResponse
from django.conf import settings
from .models import Archivo
from django.contrib.auth.models import User
import json

from io import BytesIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO
import base64

from gtts import gTTS

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Usuario Autenticado')
                else:
                    return HttpResponse('Este usuario no esta activo')
            else:
                return HttpResponse('Error de autenticación')
    else:
        form=LoginForm()
        return render(request,'incluLectora/loginNormal.html',{'form':form})
            

def pagina_principal(request):
    return render(request, 'incluLectora/principal.html')


@login_required
def dashboard(request):
    return render(request,'incluLectora/dashboard.html')

@login_required
def repositorio(request):
    # Obtener todos los archivos del usuario actual
    archivos_usuario = Archivo.objects.filter(usuario=request.user)

    # Pasar los archivos a la plantilla para su renderización en HTML
    context = {'archivos_usuario': archivos_usuario}
    
    # Renderizar la plantilla con los archivos del usuario
    return render(request, 'incluLectora/repositorio.html', context)


def register(request):
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'incluLectora/register_done.html',{'new_user':new_user})
    else:
        user_form=UserRegistrationForm()
        return render(request,'incluLectora/register.html',{'user_form':user_form}) 
    


def extract_text_from_uploaded_pdf_helper(pdf_file_obj):
    output_string = StringIO()
    laparams = LAParams()  # Puedes ajustar los parámetros de diseño según tus necesidades
    extract_text_to_fp(pdf_file_obj, output_string, output_type='text', codec='utf-8', laparams=laparams)
    output_string.seek(0)
    text = output_string.read().strip()
    output_string.close()
    return text

def cargar_pdf(request):
    if request.method == 'POST' and request.FILES.get('archivo_pdf'):
        pdf_file = request.FILES['archivo_pdf']
        pdf_file_bytes = pdf_file.read()
        pdf_file_obj = BytesIO(pdf_file_bytes)
        text = extract_text_from_uploaded_pdf_helper(pdf_file_obj)
        
        # Puedes hacer cualquier otra cosa con la variable 'extracted_text' aquí
        ruta_archivo = os.path.join(settings.BASE_DIR, './incluLectora/static/tmp', 'archivo.txt')

        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(text)
        archivo.close()

        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            text = archivo.read()

        # Convertir el texto extraído a audio
        language = 'es-us'
        speech = gTTS(text=text, lang=language, slow=False)
        
        # Crear un objeto BytesIO para almacenar el audio en memoria
        audio_bytes = BytesIO()
        speech.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        
        # Codificar los bytes del audio en Base64
        audio_base64 = base64.b64encode(audio_bytes.getvalue()).decode('utf-8')
        print("correcto hasta aqui:", text)
        # Devolver respuesta JSON con el mensaje de texto y el audio en formato Base64
        return JsonResponse({'mensaje': text, 'audio': audio_base64}, status=200)

    else:
        print("error en el pdf")
        return JsonResponse({'mensaje': 'Error: No se recibió el archivo PDF'}, status=400)

def guardar_archivos(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario')  # Obtener el ID de usuario serializado

        try:
            usuario = User.objects.get(id=usuario_id)  # Obtener la instancia de User
        except User.DoesNotExist:
            return JsonResponse({'error': f'El usuario con ID "{usuario_id}" no existe'}, status=404)

        archivo_txt = request.FILES.get('archivo_txt')
        archivo_audio = request.FILES.get('archivo_audio')

        # Crear una instancia de Archivo y guardar los datos
        nuevo_archivo = Archivo(usuario=usuario, archivo_txt=archivo_txt, archivo_audio=archivo_audio)
        nuevo_archivo.save()

        return JsonResponse({'mensaje': 'Archivos guardados correctamente'}, status=200)
    else:
        return JsonResponse({'error': 'Error al guardar'}, status=405)
