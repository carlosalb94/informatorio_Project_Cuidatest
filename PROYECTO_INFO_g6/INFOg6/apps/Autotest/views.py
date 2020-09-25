from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import AltaAutotest, AltaSolicitud,CargaResultadosForm
from .models import Autotest, Solicitud


# VISTA BASADA EN FUNCIONES


def validarAutotest(unAutotest):
	contador = 0
	sintomas = [unAutotest.tosSeca,unAutotest.fiebre,unAutotest.dolordeGarganta,unAutotest.contactoConPositivo,
				unAutotest.dolorCabeza,unAutotest.dificultadRespiratoria,unAutotest.alteracionGustoOfalto,
				unAutotest.mucosidad,unAutotest.enfermedad,unAutotest.vomitos,unAutotest.diarrea,unAutotest.dolorCorporal]

	for s in sintomas:
		if s: 
			contador += 1

		if contador>3:
			return True

	return False
	

# VISTAS BASADAS EN CLASES

class Autotest(CreateView):
	model = Autotest
	form_class = AltaAutotest
	template_name = 'Autotest/crear.html'
	success_url = reverse_lazy('Autotest:final')
	inc_url = reverse_lazy('Autotest:inc_final')
	
	def form_valid(self, form):
		unAutotest = form.save(commit = False)
		unAutotest.usuario = self.request.user
		unAutotest.corresponde_hisopado = validarAutotest(unAutotest)
		unAutotest.save()
		print(unAutotest.corresponde_hisopado)
		if  unAutotest.corresponde_hisopado:
			Solicitud.objects.create(usuario= unAutotest.usuario,autotest=unAutotest)
			return redirect(self.success_url)
	
		return redirect(self.inc_url)

		
# class ListarSolicitudes(ListView): 
# 	model = Solicitud 
# 	template_name = 'autotest/listarsolicitudes.html'
	
def ListarSolicitudes(request): 
	context = {}
	todos = Solicitud.objects.all()
	context['solicitudes'] = todos

	return render(request,'Autotest/listarsolicitudes.html',context)

def CargaResultados(request): 
	context = {}
	todos = Solicitud.objects.all()
	context['solicitudes'] = todos

	return render(request,'Autotest/carga_resultados.html',context)

class Modificar(UpdateView):
	model = Solicitud
	form_class = CargaResultadosForm
	template_name = 'Autotest/modificar.html'
	success_url = reverse_lazy('Autotest:resultados')


# COMO TRANSEFIR EL ID_AUTOTEST AL MOMENTO DE DAR DE ALTA UNA SOLICITUD