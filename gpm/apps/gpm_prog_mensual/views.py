from django.shortcuts import render


def todos(request):
    return render(request, 'gpm_programa_mensual/todos.html')

