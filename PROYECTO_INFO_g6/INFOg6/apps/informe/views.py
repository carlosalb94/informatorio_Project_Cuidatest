from django.shortcuts import render

# Create your views here.

from apps.Autotest.models import Autotest, Solicitud
from apps.users.models import Localidad, Usuario


def ListarAutotest(request):

	context = {}
	todos = Autotest.objects.all()
	context['autotest'] = todos

	return render(request, 'informe/todos.html', context) 


def ListarXLocalidad(request):
	
	context = {}
	localidades = Localidad.objects.all()
	context['localidades'] = localidades


	localidad = request.GET.get("filtro", None)  #retorna el id en string en un queryset

	print(localidad[0])

	usuarios = Usuario.objects.filter(localidad= localidad[0])

	resultado1 = []


	for u in usuarios:

		re = Autotest.objects.filter(usuario = u)
		resultado1.append(re[0])

	context['autotest'] = resultado1

	return render(request, 'informe/listarXLocalidad.html', context)




	