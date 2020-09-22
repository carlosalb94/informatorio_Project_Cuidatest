from django.db import models
# from users.models import *
# Create your models here.

class Autotest(models.Model):
	id_usuario = models.ForeignKey('users.Usuario',on_delete=models.CASCADE)
	tosSeca= models.BooleanField(verbose_name= 'Tos seca', null=True)
	fiebre = models.BooleanField(verbose_name='Fiebre', null=True)
	dolordeGarganta = models.BooleanField(verbose_name='Dolor de garganta', null=True)
	dolorCorporal = models.BooleanField(verbose_name='Dolor corporal', null=True)
	contactoConPositivo = models.BooleanField(verbose_name='Contacto con una persona covid positivo', null=True)
	dolorCabeza = models.BooleanField(verbose_name='Dolor de cabeza', null=True)
	dificultadRespiratoria = models.BooleanField(verbose_name='Dificultad respiratoria', null=True)
	alteracionGustoOfalto = models.BooleanField(verbose_name='Alteración gusto/olfato', null=True)
	mucosidad = models.BooleanField(verbose_name='Mucosidad', null=True)
	enfermedad = models.BooleanField(verbose_name='Enfermedad preexistente', null=True)
	vomitos = models.BooleanField(verbose_name='Vomitos o nauseas', null=True)
	diarrea = models.BooleanField(verbose_name='Diarrea', null=True)
	texto = models.TextField(max_length=200, verbose_name='Sintomas/Información que desee agregar', null=True)
	corresponde_hisopado = models.BooleanField(null=True)


	


class Solicitud(models.Model):

	id_solicitud = models.AutoField(primary_key=True)
	id_autotest = models.ForeignKey('Autotest.Autotest', on_delete=models.CASCADE)
	id_usuario = models.OneToOneField('users.Usuario', on_delete=models.CASCADE)
	resultado = models.BooleanField(null=True)
	estado = models.IntegerField(default=1, null=False)
	fecha_creacion = models.DateField()
	fecha_hisopado = models.DateField(default=True)







