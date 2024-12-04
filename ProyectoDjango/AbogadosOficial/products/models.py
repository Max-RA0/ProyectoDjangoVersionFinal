from django.db import models

# Modelo base para servicios legales
class ServicioLegal(models.Model):
    _nombre_servicio = models.CharField(  # Privatizado
        max_length=255,
        unique=True,
        db_column='nombre_servicio',
    )
    _descripcion = models.CharField(  # Privatizado
        max_length=255,
        db_column='descripcion',
    )
    _costo = models.DecimalField(  # Privatizado
        max_digits=10,
        decimal_places=2,
        db_column='costo',
    )
    
    def get_nombre_servicio(self):
        return self._nombre_servicio

    def get_descripcion(self):
        return self._descripcion

    def get_costo(self):
        return self._costo
    
    def _mostrar_info(self):  # Privatizado
        return (
            f"Nombre: {self._nombre_servicio}, Descripción: {self._descripcion}, "
        )

    def __str__(self):  # Se mantiene público para Django Admin
        return self._nombre_servicio

    class Meta:
        abstract = False
        verbose_name = "Servicio Legal"
        verbose_name_plural = "Servicios Legales"


# Modelo específico para servicios de divorcio
class Divorcio(ServicioLegal):
    _num_divorcios = models.IntegerField(  # Privatizado
        db_column='num_divorcios',
    )
    _duracion_estimada = models.DecimalField(  # Privatizado
        max_digits=5,
        decimal_places=2,
        db_column='duracion_estimada',
    )
    
    def get_num_divorcios(self):
        return self._num_divorcios

    def get_duracion_estimada(self):
        return self._duracion_estimada
    
    def _mostrar_info(self):  # Privatizado
        return (
            f"Nombre: {self._nombre_servicio}, Descripción: {self._descripcion}, "
            f"Costo: {self._costo}, Número de Divorcios: {self._num_divorcios}, "
            f"Duración Estimada: {self._duracion_estimada} años, "
        )

    @staticmethod
    def _calcular_impuesto(costo, num_divorcios):  # Privatizado
        return costo * num_divorcios

    class Meta:
        verbose_name = "Servicio de Divorcio"
        verbose_name_plural = "Servicios de Divorcio"


# Modelo específico para asesorías legales
class AsesoriaLegal(ServicioLegal):
    _num_asesorias = models.IntegerField(  # Privatizado
        db_column='num_asesorias',
    )
    _especialidad = models.CharField(  # Privatizado
        max_length=255,
        db_column='especialidad',
    )
    
    def get_num_asesorias(self):
        return self._num_asesorias

    def get_especialidad(self):
        return self._especialidad
    
    def _mostrar_info(self):  # Privatizado
        return (
            f"Nombre: {self._nombre_servicio}, Descripción: {self._descripcion}, "
            f"Costo: {self._costo}, Especialidad: {self._especialidad}, "
        )

    @staticmethod
    def _calcular_impuestos(costo, num_asesorias):  # Privatizado
        return costo * num_asesorias

    class Meta:
        verbose_name = "Asesoría Legal"
        verbose_name_plural = "Asesorías Legales"
