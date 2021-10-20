"""Persianas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name="index"),
        path('JM_PAG_2/', views.JM_PAG_2, name= "JM_PAG_2"),
        path('modelos/<int:id_categoria>/', views.modelos_categoria, name="modelos.categoria"),
        path("login/", auth_views.LoginView.as_view(template_name="login/login.html"),name="login"), 
        path('Crear_Contacto/', views.Crear_Contacto, name="Crear_Contacto"),
        path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="login"),       
]

