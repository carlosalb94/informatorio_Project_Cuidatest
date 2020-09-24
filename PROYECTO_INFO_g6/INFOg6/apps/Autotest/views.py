from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import AltaAutotest, AltaSolicitud
from .models import Autotest, Solicitud


# VISTA BASADA EN FUNCIONES
def final(request):
	return render(request, 'Autotest/final.html') 

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

# class Solicitud(CreateView):
# 	model = Solicitud
# 	form_class = AltaSolicitud

class Autotest(CreateView):
	model = Autotest
	form_class = AltaAutotest
	template_name = 'Autotest/crear.html'
	success_url = reverse_lazy('Autotest:final')
	
	def form_valid(self, form):
		unAutotest = form.save(commit = False)
		unAutotest.usuario = self.request.user
		unAutotest.corresponde_hisopado = validarAutotest(unAutotest)
		unAutotest.save()
		if  unAutotest.corresponde_hisopado:
			Solicitud.objects.create(usuario= unAutotest.usuario,autotest=unAutotest)

		return redirect(self.success_url)


class ListarSolicitudes(ListView): 
	model = Solicitud 
	template_name = 'autotest/listarsolicitudes.html'
	
# COMO TRANSEFIR EL ID_AUTOTEST AL MOMENTO DE DAR DE ALTA UNA SOLICITUD