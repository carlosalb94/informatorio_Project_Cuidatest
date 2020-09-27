
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('Login',auth.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('Logout',auth.LogoutView.as_view(),name="logout"),
    path('reset_password/',auth.PasswordResetView.as_view(template_name='users/password_reset_form.html'),name="reset_password"),
    path('reset_password_sent/',auth.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name="password_reset_confirm"),
    path('reset_password_complete/',auth.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name="password_reset_complete"),
    # URLS DE APLICACIONES
    path('Autotest/',include('apps.Autotest.urls')),
    path('users/', include('apps.users.urls')),
    path('informe/', include('apps.informe.urls')),
]
