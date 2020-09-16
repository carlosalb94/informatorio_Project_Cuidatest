from django import forms

from .models import Autotest, Solicitud

class AltaAutotest(forms.ModelForm):

	class Meta:
		model = Autotest
		fields = ['tosSeca', 'fiebre', 'dolorCabeza','dolorCorporal', 'contactoConPositivo',
					'dificultadRespiratoria', 'enfermedad','vomitos','diarrea','dolordeGarganta',
					'alteracionGustoOfalto','texto',
				]

class AltaSolicitud(forms.ModelForm):

	class Meta:
		model = Solicitud
		fields = ['__all__']

