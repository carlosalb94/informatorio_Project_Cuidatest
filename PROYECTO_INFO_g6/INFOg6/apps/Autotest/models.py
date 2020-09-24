from django.db import models

# from users.models import *
# Create your models here.

class Autotest(models.Model):

	usuario = models.ForeignKey('users.Usuario',on_delete=models.CASCADE)

	tosSeca= models.BooleanField(verbose_name= 'Tos seca')
	fiebre = models.BooleanField(verbose_name='Fiebre')
	dolordeGarganta = models.BooleanField(verbose_name='Dolor de garganta')
	dolorCorporal = models.BooleanField(verbose_name='Dolor corporal')
	contactoConPositivo = models.BooleanField(verbose_name='Contacto con una persona covid positivo')
	dolorCabeza = models.BooleanField(verbose_name='Dolor de cabeza')
	dificultadRespiratoria = models.BooleanField(verbose_name='Dificultad respiratoria')
	alteracionGustoOfalto = models.BooleanField(verbose_name='Alteración gusto/olfato')
	mucosidad = models.BooleanField(verbose_name='Mucosidad')
	enfermedad = models.BooleanField(verbose_name='Enfermedad preexistente')
	vomitos = models.BooleanField(verbose_name='Vomitos o nauseas')
	diarrea = models.BooleanField(verbose_name='Diarrea')
	corresponde_hisopado = models.BooleanField(null=True)

	



class Solicitud(models.Model):

	autotest = models.ForeignKey('Autotest.Autotest', on_delete=models.CASCADE)
	usuario = models.ForeignKey('users.Usuario', on_delete=models.CASCADE) 
	
	resultado = models.BooleanField(null=True)
	estado = models.IntegerField(default=1, null=False)   # 1 = Pendiente de hisopar / 2 = Hisopado  / 3 = Resultado Cargado
	fecha_creacion = models.DateTimeField(auto_now_add = True)
	fecha_hisopado = models.DateTimeField(null= True)

	def __str__(self):
		pass







