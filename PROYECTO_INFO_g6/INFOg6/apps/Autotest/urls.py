
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Autotest'


urlpatterns = [
	path('Autotest/', views.Autotest.as_view(template_name= "Autotest/crear.html"), name='crear' ),
	path('finTest/', views.Autotest.as_view(template_name="Autotest/final.html"), name='final'),
	path('IncorrectTest/', views.Autotest.as_view(template_name="Autotest/inc_final.html"), name='inc_final'),
	path('listarSolicitudes/', views.ListarSolicitudes, name = 'listarSolicitudes'),
	path('NoHaySolicitudes/', views.ListarSolicitudes, name='listarSolicitudes'),
	path('CargaResultados/', views.CargaResultados, name = 'resultados'),
	path('Modificar/<str:pk>', views.Modificar.as_view(), name="modificar"),
	path('pendiente/', views.evaluarSolicitudPendiente, name='pendiente'),
]