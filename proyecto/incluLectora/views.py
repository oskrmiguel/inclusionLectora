import os
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from django.http import JsonResponse
from django.conf import settings
import PyPDF2
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
    


def cargar_pdf(request):
    if request.method == 'POST' and request.FILES.get('archivo_pdf'):
        # Lógica para manejar el archivo PDF
        archivo_pdf = request.FILES['archivo_pdf']

        # Abrir el archivo PDF en modo binario ('rb')
        with archivo_pdf.open("rb") as pdf:
            # Crear un objeto PdfReader
            reader = PyPDF2.PdfReader(pdf)

            # Obtener el número total de páginas en el PDF
            total_pages = len(reader.pages)

            # Crear una variable para almacenar el texto extraído
            extracted_text = ""

            # Iterar sobre todas las páginas y extraer el texto
            for page_number in range(total_pages):
                # Obtener la página específica
                page = reader.pages[page_number]

                # Extraer el texto de la página y agregarlo a la variable
                extracted_text += page.extract_text()

        # Puedes hacer cualquier otra cosa con la variable 'extracted_text' aquí
        ruta_archivo = os.path.join(settings.BASE_DIR, './incluLectora/static/tmp', 'archivo.txt')

        text = extracted_text.encode('utf-8')
        print(text.decode("utf-8"))

        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(text.decode("utf-8").rstrip("\n"))
        archivo.close()

        ruta_archivo = os.path.join(settings.BASE_DIR, './incluLectora/static/tmp', 'archivo.txt')

        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            text = archivo.read()

        language = 'es-us'
        speech = gTTS(text=text, lang=language, slow=False)
        # Guardar el archivo de audio
        speech.save("./incluLectora/static/tmp/audio.mp3")

        # Devolver respuesta JSON con el texto extraído
        return JsonResponse({'mensaje': extracted_text})
    else:
        return JsonResponse({'mensaje': 'Error: No se recibió el archivo PDF'}, status=400)

        