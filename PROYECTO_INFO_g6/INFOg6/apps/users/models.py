from django.db import models

from django.contrib.auth.models import AbstractUser


class Localidad(models.Model):
	
	nombre = models.CharField(max_length = 40, verbose_name = 'nombre localidad', null=False)
	cant_habitantes = models.IntegerField(verbose_name = 'cantidad de habitantes', null=False) 

	def __str__(self):
		return f'{self.nombre}'
		


class Usuario(AbstractUser):
	
	localidad = models.ForeignKey('Localidad', on_delete=models.SET_NULL, null=True)
	
	last_name = models.CharField(max_length=30, verbose_name = 'apellido')
	first_name = models.CharField(max_length=150, verbose_name = 'nombre')
	fecha_nac = models.DateTimeField(null=True ,verbose_name='fecha de nacimiento', default= '01/01/2020', help_text='ejemplo: 25/11/2002')
	dni = models.IntegerField()
	telefono = models.BigIntegerField()
	domicilio = models.CharField(max_length=70, default='Su direccion: Av. Ejemplo 1234')
	REQUIRED_FIELDS = ['email','telefono', 'domicilio','dni', 'first_name', 'last_name']









