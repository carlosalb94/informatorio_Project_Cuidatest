
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('Contacto',views.Contacto,name="contacto"),
    path('Login',views.Login,name="login"),
    path('Registro',views.Registro,name="registro"),

    # URLS DE APLICACIONES
    path('Productos',include('apps.productos.urls'))
]
