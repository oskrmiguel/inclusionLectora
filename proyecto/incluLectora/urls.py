from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('login/',views.user_login,name='login')    Es del modelo creado por nosotros
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    #path('principal/', views.pagina_principal, name='principal'),
    #path('', include('django.contrib.auth.urls')),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('',views.pagina_principal,name='principal'),
    path('register/',views.register,name='register'),
    path('dashboard/pdf', views.cargar_pdf, name='cargar_pdf'),
    path('dashboard/guardar_archivos', views.guardar_archivos, name='guardar_archivos'),
    path('respositorio/',views.repositorio,name='repositorio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
