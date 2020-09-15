from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import AltaAutotest
from .models import Autotest


# VISTA BASADA EN FUNCIONES
def final(request):
	return render(request, 'Autotest/final.html') 



# VISTAS BASADAS EN CLASES
class Autotest(CreateView):
	model = Autotest
	form_class = AltaAutotest
	template_name = 'Autotest/crear.html'
	success_url = reverse_lazy('Autotest:final')

	def form_valid(self, form):
		u = form.save(commit = False)
		u.id_usuario = self.request.user
		u.save()
		return redirect(self.success_url)
