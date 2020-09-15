from django.db import models

from django.contrib.auth.models import AbstractUser


class Localidad(models.Model):
	id_localidad = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length = 40, verbose_name = 'nombre localidad', null=False)
	cant_habitantes = models.IntegerField(verbose_name = 'cantidad de habitantes', null=False) 


class Usuario(AbstractUser):
	last_name = models.CharField(max_length=30, verbose_name = 'apellido')
	first_name = models.CharField(max_length=150, verbose_name = 'nombre')
	fecha_nac = models.DateField(null=True ,verbose_name='fecha de nacimiento')
	dni = models.IntegerField()
	id_localidad = models.ForeignKey('Localidad', on_delete=models.SET_NULL, null=True)
	telefono = models.IntegerField()
	domicilio = models.TextField(max_length=70, default=True)
	REQUIRED_FIELDS = ['email','telefono', 'domicilio','dni', 'first_name', 'last_name']









