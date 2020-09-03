from django import forms

from .models import Autotest

class AltaAutotest(forms.ModelForm):

	class Meta:
		model = Autotest
		fields = '__all__'