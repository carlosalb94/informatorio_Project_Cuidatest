from django.shortcuts import render


def Home(request):
	return render(request,'home.html')

def Contacto(request):
	return render(request,'contacto.html')

def Login(request):
	return render(request,'login.html')

def Registro(request):
	return render(request,'registro.html')

