from django.db import models

# Create your models here.

class Autotest(models.Model):
	tosSeca= models.BooleanField(verbose_name= 'Tos seca', null=True)
	fiebre = models.BooleanField(verbose_name='Fiebre', null=True)
	dolorCabeza = models.BooleanField(verbose_name='Dolor de cabeza', null=True)
	dolorCorporal = models.BooleanField(verbose_name='Dolor corporal', null=True)
	contactoConPositivo= models.BooleanField(verbose_name='Contacto con una persona covid positivo', null=True)
	dificultadRespiratoria = models.BooleanField(verbose_name='Dificultad respiratoria', null=True)
	mucosidad= models.BooleanField(verbose_name='Mucosidad', null=True)
	enfermedad=models.BooleanField(verbose_name='Enfermedad preexistente', null=True)
	vomitos=models.BooleanField(verbose_name='Vomitos o nauseas', null=True)
	diarrea=models.BooleanField(verbose_name='Diarrea', null=True)
	dolordeGarganta=models.BooleanField(verbose_name='Dolor de garganta', null=True)
	alteracionGustoOfalto=models.BooleanField(verbose_name='Alteración gusto/olfato', null=True)
	texto = models.TextField(max_length=200, verbose_name='Sintomas/Información que desee agregar', null=True)
	corresponde_hisopado = models.BooleanField(null=True)

