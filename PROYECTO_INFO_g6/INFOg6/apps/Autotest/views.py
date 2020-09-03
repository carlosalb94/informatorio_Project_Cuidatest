from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import AltaAutotest
from .models import Autotest


# VISTA BASADA EN FUNCIONES

# VISTAS BASADAS EN CLASES
class Autotest(CreateView):
	model = Autotest
	form_class = AltaAutotest
	template_name = 'Autotest/crear.html'
	success_url = reverse_lazy('home')

