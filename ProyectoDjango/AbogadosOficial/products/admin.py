from django.contrib import admin
from .models import Divorcio, AsesoriaLegal

@admin.register(Divorcio)
class DivorcioAdmin(admin.ModelAdmin):
    list_display = ('_nombre_servicio', '_costo', '_num_divorcios')  # Ajusta con los nombres internos

@admin.register(AsesoriaLegal)
class AsesoriaLegalAdmin(admin.ModelAdmin):
    list_display = ('_nombre_servicio', '_costo', '_especialidad')  # Ajusta con los nombres internos
