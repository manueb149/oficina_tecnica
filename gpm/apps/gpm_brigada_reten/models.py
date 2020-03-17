from django.db import models


class Empleado(models.Model):
    zona = [
        ('ADM','Administrativa'),
        ('NORTE', 'Zona Norte'),
        ('SUR', 'Zona Sur'),
        ('ESTE', 'Zona Este'),
        ('LAB', 'Laboratorio'),
        ('AUTO', 'Automatizacion'),
        ('N/A', 'No asignado'),
    ]
    id = models.AutoField(primary_key=True)
    no_empleado = models.IntegerField('Carnet', blank=False, null=False)
    nombres = models.CharField('Nombres', max_length=100, blank=False, null=False)
    apellidos = models.CharField('Apellidos',max_length=100, blank=False, null=False)
    cargo = models.CharField('Cargo', max_length=255, blank=False, null=False)
    no_flota = models.CharField('Numero Flota', max_length=13, blank=True, null=True)
    no_movil = models.CharField('Numero Celular', max_length=13, blank=True, null=True)
    vehiculo = models.CharField('Tipo de Vehiculo', max_length=100, blank=True, null=True)
    ficha_vehiculo = models.IntegerField('Ficha del Vehiculo', blank=True, null=True)
    correo = models.EmailField('Correo Electronico', max_length=254, blank=True, null=True)
    area = models.CharField('Area de trabajo', max_length=50, choices=zona, default='N/A')
    estado = models.BooleanField('Activo/Inactivo',default=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
    def __str__(self):
        return "{0}, {1}".format(self.apellidos, self.nombres)

