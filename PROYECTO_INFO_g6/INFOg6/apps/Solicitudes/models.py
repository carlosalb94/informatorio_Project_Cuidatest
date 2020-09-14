from django.db import models
#from Autotest.models import *
#from users.models import *
# Create your models here.


class Solicitud(models.Model):

	id_solicitud = models.AutoField(primary_key=True)
	id_autotest = models.ForeignKey('Autotest.Autotest', on_delete=models.CASCADE)
	id_usuario = models.OneToOneField('users.Usuario', on_delete=models.CASCADE)
	resultado = models.BooleanField(null=True)
	fecha_creacion = models.DateField()
	fecha_hisopado = models.DateField(default=True)


