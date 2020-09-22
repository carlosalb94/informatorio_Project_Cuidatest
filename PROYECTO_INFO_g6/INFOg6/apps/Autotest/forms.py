from django import forms

from .models import Autotest, Solicitud

class AltaAutotest(forms.ModelForm):

	class Meta:
		model = Autotest
		fields = ['tosSeca', 'fiebre', 'dolorCabeza','dolorCorporal', 'contactoConPositivo',
					'dificultadRespiratoria', 'enfermedad','mucosidad','vomitos','diarrea','dolordeGarganta',
					'alteracionGustoOfalto','texto',
				]

class AltaSolicitud(forms.ModelForm):

	class Meta:
		model = Solicitud
		fields = '__all__'


	def save(self,commit=True):
			autotest= super().save()
			Solicitud.objects.create(id_autotest_id =8,
									id_usuario_id =4)
			return autotest
		
