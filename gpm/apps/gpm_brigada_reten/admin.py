from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class EmpleadoResource(resources.ModelResource):
    class Meta:
        model=Empleado


class EmpleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # resource_class = EmpleadoResource
    search_fields = ['nombres', 'apellidos', 'no_empleado', 'ficha_vehiculo']
    list_display = ('no_empleado', 'nombres', 'apellidos', 'area', 'cargo', 'vehiculo', 'ficha_vehiculo', 'estado')


admin.site.register(Empleado, EmpleadoAdmin)
