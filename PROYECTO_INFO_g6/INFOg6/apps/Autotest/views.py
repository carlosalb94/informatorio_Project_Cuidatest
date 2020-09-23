from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import AltaAutotest, AltaSolicitud
from .models import Autotest, Solicitud


# VISTA BASADA EN FUNCIONES
def final(request):
	return render(request, 'Autotest/final.html') 

def validarAutotest(u):
	contador = 0
	sintomas = [u.tosSeca, u.fiebre, u.dolordeGarganta, u.contactoConPositivo, u.dolorCabeza, 
				u.dificultadRespiratoria, u.alteracionGustoOfalto, u.mucosidad, u.enfermedad,
				u.vomitos, u.diarrea, u.dolorCorporal]

	for s in sintomas:
		print(s)
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
		u = form.save(commit = False)
		u.id_usuario = self.request.user
		u.corresponde_hisopado = validarAutotest(u)
		u.save()
		Solicitud.objects.create(id_usuario=u.id_usuario,id_autotest=u)
		return redirect(self.success_url)


class ListarSolicitudes(ListView): 
	model = Solicitud 
	template_name = 'autotest/listarsolicitudes.html'
	
# COMO TRANSEFIR EL ID_AUTOTEST AL MOMENTO DE DAR DE ALTA UNA SOLICITUD