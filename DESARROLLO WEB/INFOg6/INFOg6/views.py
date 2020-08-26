from django.shortcuts import render

def Home(request):
    return render(request,'home.html')

def Pag2(request):
    return render(request,'pag2.html')