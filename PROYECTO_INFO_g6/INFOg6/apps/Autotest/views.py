from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import AltaAutotest , AltaSolicitud
from .models import Autotest, Solicitud


# VISTA BASADA EN FUNCIONES
def final(request):
	return render(request, 'Autotest/final.html') 

def validarAutotest(u):
	if u.tosSeca  and u.dolorCorporal and u.fiebre:
		return True
	else:
		return False


# VISTAS BASADAS EN CLASES
'''
class Solicitud(CreateView):
	model = Solicitud
	form_class = AltaSolicitud

	def form_valid(self, form):
		u = form.save(commit = False)
		u.id_autotest = None
		u.id_usuario = self.request.user
		u.resultado = None
		u.fecha_creacion = '05/05/1994'
		u.fecha_hisopado = None
'''

class Autotest(CreateView):
	model = Autotest
	form_class = AltaAutotest
	template_name = 'Autotest/crear.html'
	success_url = reverse_lazy('Autotest:final')
	
	

	def form_valid(self, form):
		u = form.save(commit = False)
		u.id_usuario = self.request.user
	#	u.corresponde_hisopado = validarAutotest(u)
	#	if u.corresponde_hisopado:
	#		s = Solicitud()
		u.save()
		return redirect(self.success_url)

	

# COMO TRANSEFIR EL ID_AUTOTEST AL MOMENTO DE DAR DE ALTA UNA SOLICITUD