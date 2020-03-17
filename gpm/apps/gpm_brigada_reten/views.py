from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import *
from .files.excel import *

#GLOBAL VARIABLES
empleados = []
file = ""


def listado_personal(request):
    empleados = Empleado.objects.filter(estado=True)
    return render(request, 'gpm_brigada_reten/listado_personal.html', {'empleados': empleados})


def brigada_semanal(request):
    global empleados
    empleados = []
    e_norte = Empleado.objects.filter(area='NORTE', estado=True)
    e_sur = Empleado.objects.filter(area='SUR', estado=True)
    e_este = Empleado.objects.filter(area='ESTE', estado=True)
    return render(request, 'gpm_brigada_reten/brigada_semanal.html', {'norte':e_norte, 'sur':e_sur, 'este':e_este})

def get_empleados(request):
    global empleados, file
    if request.is_ajax():
        if request.method == 'GET':
            data = request.GET
            print(data)
            ids = data.getlist('empleados[]')
            date = str(ids.pop(-1)) 
            print(date)
            ids = list(map(int, ids))
            empleados = Empleado.objects.filter(no_empleado__in=ids)
            wb = load_workbook(open_file_location())
            ws = wb.active
            ws.title = 'Brigada Reten'
            ws['A3'] = 'Personal de Retén del '+ date
            row = 7
            for empleado in empleados.filter(area='NORTE', estado=True):
                writeRow(row, empleado, ws)
                row+=1
            for empleado in empleados.filter(area='SUR', estado=True):
                writeRow(row, empleado, ws)
                row+=1
            for empleado in empleados.filter(area='ESTE', estado=True):
                writeRow(row, empleado, ws)
                row+=1
            wb.save(save_file_location())
            file = save_file_location()
    return render(request, 'gpm_brigada_reten/seleccion.html', {'empleados': empleados, 'file': file})

def get_excel(request):
    if request.is_ajax():
        if request.method == 'GET':
            data = request.GET.getlist('data')
            print(data)
            response = HttpResponse(
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            )
            response['Content-Disposition'] = 'attachment; filename=hola.xlsx'
            wb = Workbook()
            ws = wb.active
            ws.title='Hola'
            ws.cell(1,1,value='Hola')
            wb.save(response)
            return HttpResponse(response)
    else:
        return HttpResponse('ERROR!')        

