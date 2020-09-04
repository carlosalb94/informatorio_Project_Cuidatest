from django.db import models

# Create your models here.


class Solicitud(models.Model):

	id_solicitud = models.AutoField(primary_key=True)
	id_autotest = models.IntegerField()
	id_usuario = models.IntegerField()
	resultado = models.BooleanField(null=True)
	fecha_creacion = models.DateField()
	fecha_hisopado = models.DateField(default=True)


