from django.shortcuts import render

def Home(request):
    return render(request,'home.html')

def Registro(request):
	return render(request, 'registro.html')



