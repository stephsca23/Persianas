from rest_framework import serializers

from .models import Categoria, Modelo, Servicios


class ModeloSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Tour """
    class Meta:
        # Se define sobre que modelo actúa
        model = Modelo
        # Se definen los campos a incluir
        fields = ('nombre', 'precio', 'ventajas', 'desventajas', 'habitacion','img')


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Zona """

    # Se define la relación de una zona y sus tours realizados
    modelos = ModeloSerializer(many=True, read_only=True)

    class Meta:
        # Se define sobre que modelo actua
        model = Categoria
        # Se definen los campos a incluir
        fields = ('nombre', 'modelos')


class ServiciosSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Zona """

    class Meta:
        # Se define sobre que modelo actua
        model = Servicios
        # Se definen los campos a incluir
        fields = ('nombre', 'descripcion')
