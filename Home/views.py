from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Modelo, Categoria, Servicios


from .serializers import CategoriaSerializer, ModeloSerializer, ServiciosSerializer
from rest_framework import viewsets



def index(request):
      tipos = Categoria.objects.all()
      servicios = Servicios.objects.all()
      
      return render (request, "home1/index.html", {"categorias":tipos, "servicios": servicios})

@login_required()
def JM_PAG_2( request):
   modelos = Modelo.objects.filter(habitacion__nombre = "sala")
   return render (request, "hHome/JM_PAG_2.html", {"modelos": modelos})


@login_required()
def modelos_categoria (request, id_categoria):
	# return render(request, "Home/JM_PAG_2.html")

# Create your views here.
   categoria = Categoria.objects.get(pk=id_categoria)
   modelos = Modelo.objects.filter(habitacion=categoria)
   return render (request, "Home/JM_PAG_2.html", {"modelos":modelos, "categoria": categoria})

def Crear_Contacto (request):


      return render (request, "contacto/Crear_Contacto.html")


class CategoriaViewSet(viewsets.ModelViewSet):
   """
   API que permite realizar operaciones en la tabla Zona
   """
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre todos las Zonas disponibles.
   queryset = Categoria.objects.all().order_by('nombre')
   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = CategoriaSerializer


class ModeloViewSet(viewsets.ModelViewSet):
   """
   API que permite realizar operaciones en la tabla Tour
   """
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre todos los tours disponibles.
   queryset = Modelo.objects.all().order_by('precio')
   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = ModeloSerializer


class ServiciosViewSet(viewsets.ModelViewSet):
   """
   API que permite realizar operaciones en la tabla Tour
   """
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre todos los tours disponibles.
   queryset = Servicios.objects.all().order_by('nombre')
   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = ServiciosSerializer