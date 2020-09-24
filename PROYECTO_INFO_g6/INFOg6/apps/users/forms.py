
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
	fecha_nac = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
	class Meta:
		model = Usuario
		fields = ['username','email','first_name',
				'last_name','password1','password2', 
				'localidad', 'telefono', 'dni', 'fecha_nac']