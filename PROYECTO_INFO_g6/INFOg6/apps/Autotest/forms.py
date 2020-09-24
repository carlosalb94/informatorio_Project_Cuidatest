from django import forms
from datetime import date

from .models import Autotest, Solicitud

class AltaAutotest(forms.ModelForm):

	class Meta:
		model = Autotest
		fields = ['tosSeca', 'fiebre', 'dolorCabeza','dolorCorporal', 'contactoConPositivo',
					'dificultadRespiratoria', 'enfermedad','mucosidad','vomitos','diarrea','dolordeGarganta',
					'alteracionGustoOfalto',
				]
	
class AltaSolicitud(forms.ModelForm):

	class Meta:
		model = Solicitud
		fields = '__all__'


