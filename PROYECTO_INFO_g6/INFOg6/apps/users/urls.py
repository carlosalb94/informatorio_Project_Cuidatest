from django.contrib import admin
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
	path('Registrar/', views.RegistroUsuario.as_view(), name= "registro" )
]