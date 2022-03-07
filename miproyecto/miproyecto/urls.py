"""miproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from .views import saludo,segunda_vista,dia,numero_random,numero_del_usuario,nacimiento, mi_plantilla

urlpatterns = [
    path('admin/',admin.site.urls),
    path('saludo/',saludo),
    path('',saludo),
    path('segunda',segunda_vista),
    path('dia',dia),
    path('random/',numero_random),
    path('dame-numero/<int:numero>',numero_del_usuario),
    path('edad/<int:numero>',nacimiento),
    path('mi_plantilla/',mi_plantilla),
    # path('dame-numero/<numero>',numero_del_usuario),
    # En el último no se espeifica el tipo de dato a ingresar en la URL
]
