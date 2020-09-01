from django.db import models

# Create your models here.

class Autotest(models.Model):
	tosSeca= models.BooleanField()
	fiebre = models.BooleanField()
	dolorCabeza = models.BooleanField()
	dolorCorporal = models.BooleanField()
	contactoConPositivo= models.BooleanField()
	dificultadRespiratoria = models.BooleanField()
	mucosidad= models.BooleanField()


