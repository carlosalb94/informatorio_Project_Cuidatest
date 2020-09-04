
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('Login',auth.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('Logout',auth.LogoutView.as_view(),name="logout"),

    # URLS DE APLICACIONES
    path('Autotest',include('apps.Autotest.urls')),
    path('users', include('apps.users.urls')) 
]
