"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('canal-denuncias/', views.canal_denuncias, name='canal_denuncias'),
    path('aviso-legal/', views.aviso_legal, name='aviso_legal'),
    path('lista-denuncias/', views.lista_denuncias, name='lista_denuncias'),
    path('detalle-denuncia/<int:pk>/', views.detalle_denuncia, name='detalle_denuncia'),
    path('preguntas-frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
    path('normativa/', views.normativa, name='normativa'),
    path('estado-denuncia/', views.estado_denuncia, name='estado_denuncia'),
    path('confirmacion-denuncia/<str:codigo>/', views.confirmacion_denuncia, name='confirmacion_denuncia'),
    path('buscar-denuncia/', views.buscar_denuncia, name='buscar_denuncia'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path('consultas/', views.consultas, name='consultas'),
    path('expedientes/', views.expedientes, name='expedientes'),
    path('informes/', views.informes, name='informes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
