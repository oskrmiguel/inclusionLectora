from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('login/',views.user_login,name='login')    Es del modelo creado por nosotros
    #path('login/',auth_views.LoginView.as_view(),name='login'),
    #path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    #path('password-change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    #path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('principal/', views.pagina_principal, name='principal'),
    path('', include('django.contrib.auth.urls')),
    path('',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
    path('home/', views.pagina_principal, name='home')
]
