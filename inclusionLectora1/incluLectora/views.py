from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm


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
        return render(request,'incluLectora/login.html',{'form':form})
            

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
        