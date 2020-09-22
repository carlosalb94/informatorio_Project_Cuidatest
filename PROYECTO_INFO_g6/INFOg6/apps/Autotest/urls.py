
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Autotest'


urlpatterns = [
	path('Autotest/', views.Autotest.as_view(template_name= "Autotest/crear.html"), name='crear' ),
	path('finTest/', views.final, name='final'),
	path('listarSolicitudes/', views.ListarSolicitudes.as_view(), name = "listarSolicitudes"),
]