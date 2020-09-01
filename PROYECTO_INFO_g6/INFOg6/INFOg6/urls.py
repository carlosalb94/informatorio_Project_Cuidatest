
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),



    # URLS DE APLICACIONES
    path('Autotest',include('apps.Autotest.urls')) 
]
