from django.shortcuts import render

# Create your views here.

from apps.Autotest.models import Autotest, Solicitud

def generarInforme(request):

	context = {}
	todos = Autotest.objects.all()
	context['Autotest'] = todos

	return render(request, 'informe/todos.html', context) 

	