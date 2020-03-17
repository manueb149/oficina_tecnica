from django.urls import path, include
from .views import *

urlpatterns = [
    path('listado_personal/', listado_personal, name='listado_personal'),
    path('brigada_semanal/', brigada_semanal, name='brigada_semanal'),
    path('brigada_semanal/seleccion/', get_empleados, name='seleccion'),
    path('brigada_semanal/seleccion/descarga', get_excel, name='descarga')
]
