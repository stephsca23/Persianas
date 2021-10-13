from django.contrib import admin
from .models import Usuario, Modelo, Categoria, Servicios

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ("nombre", "apellidos", "estado", "ciudad", "direccion", "email")

class ModeloAdmin (admin.ModelAdmin):
	list_display = ("nombre", "ventajas", "desventajas", "precio", "img", "habitacion")

class CategoriaAdmin (admin.ModelAdmin):
	list_display = ("nombre",)

class ServiciosAdmin (admin.ModelAdmin):
	list_display = ("nombre", "descripcion")


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Servicios, ServiciosAdmin)


