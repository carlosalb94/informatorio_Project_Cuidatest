from django.shortcuts import render

# Create your views here.
def Listar(request):
	return render(request,'productos/listar.html')