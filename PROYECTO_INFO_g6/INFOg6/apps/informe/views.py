from django.shortcuts import render

# Create your views here.

from apps.Autotest.models import Autotest, Solicitud
from apps.users.models import Localidad, Usuario


def ListarAutotest(request):

	context = {}
	todos = Solicitud.objects.all()
	context['solicitud'] = todos

	return render(request, 'informe/todos.html', context) 


def ListarXLocalidad(request):
	context = {}
	localidades = Localidad.objects.all()
	context['localidad'] = localidades
	
	id_localidad = request.GET.get('filtro',None)

	usuario = Usuario.objects.filter(id_localidad= id_localidad)

	resultado1 = []

	for u in usuario:

		resultado1.append(Autotest.objects.filter(id_usuario= u.id))

	context['autotest'] = resultado1

	return render(request, 'informe/listarXLocalidad.html', context)




	