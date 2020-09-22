
from django.contrib import admin
from django.urls import path
from . import views

app_name="informe"

urlpatterns = [
	path('listarAutotest/', views.ListarAutotest, name = "listarAutotest"),
	path('listarXLocalidad/', views.ListarXLocalidad, name = "listarXLocalidad"),

]