from django.db import models

# Create your models here.



class Usuario(models.Model):
	nombre = models.CharField(max_length=40)
	apellidos = models.CharField(max_length=80)
	estado = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=40)
	direccion = models.CharField(max_length=80)
	email = models.EmailField()
	clave = models.CharField(max_length=40)

	def __str__(self):
		return self.nombre + " " + self.apellidos


class Categoria(models.Model):
	nombre = models.CharField(max_length=45)
	
	

	def __str__(self):
		return "{}".format(self.nombre)


class Modelo(models.Model):
	nombre = models.CharField(max_length=45)
	ventajas = models.CharField(max_length=256)
	desventajas = models.CharField(max_length=256)
	precio = models.CharField(max_length =30)
	img = models.CharField(max_length=500, null=True, blank=True)
	habitacion = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="modelo_habitacion")

	
	def __str__(self):
		return self.nombre


class Servicios(models.Model):
	nombre = models.CharField(max_length=45)
	descripcion = models.CharField(max_length=260)

	def __str__(self):
		return self.nombre












