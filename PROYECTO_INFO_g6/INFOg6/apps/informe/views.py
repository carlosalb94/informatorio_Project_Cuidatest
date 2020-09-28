from django.shortcuts import render

# Create your views here.

from apps.Autotest.models import Autotest, Solicitud
from apps.users.models import Localidad, Usuario





def Informe(request):

    context={}
    context['total_autotest'] = len(Autotest.objects.all())
    context['total_solicitud'] = len(Solicitud.objects.all())
    context['tosSeca'] = len(Autotest.objects.filter(tosSeca=True))
    context['fiebre'] = len(Autotest.objects.filter(fiebre=True))
    context['dolordeGarganta'] = len(Autotest.objects.filter(dolordeGarganta=True))
    context['dolorCorporal'] = len(Autotest.objects.filter(dolorCorporal=True))
    context['contactoConPositivo'] = len(Autotest.objects.filter(contactoConPositivo=True))
    context['dolorCabeza'] = len(Autotest.objects.filter(dolorCabeza=True))
    context['dificultadRespiratoria'] = len(Autotest.objects.filter(dificultadRespiratoria=True))
    context['alteracionGustoOfalto'] =len(Autotest.objects.filter(alteracionGustoOfalto=True))
    context['mucosidad'] = len(Autotest.objects.filter(mucosidad=True))
    context['enfermedad'] = len(Autotest.objects.filter(enfermedad=True))
    context['vomitos'] = len(Autotest.objects.filter(vomitos=True))
    context['diarrea'] = len(Autotest.objects.filter(tosSeca=True))
    context['total_positivos'] = len(Solicitud.objects.filter(resultado=True))
    context['total_negativos'] = len(Solicitud.objects.filter(resultado=False))     
    
    localidades = Localidad.objects.all()
    context['localidades'] = localidades
    
    localidad = request.GET.get("filtro", None)  #retorna el id en string en un queryset
    
    if localidad:
        
        NombreLocalidad = Localidad.objects.filter(id = localidad)
        usuarios = Usuario.objects.filter(localidad= localidad[0])
        context['NombreLocalidad'] =  NombreLocalidad[0]
        resultado1 = []
        resultado2 = []

        for u in usuarios:

            re1 = Solicitud.objects.filter(usuario = u)
            re2 = Autotest.objects.filter(usuario = u)

            resultado1.append(re1[0])
            resultado2.append(re2[0])

        context['solicitudXlocalidad'] = resultado1
        context['autotestXlocalidad'] = resultado2

        cant_positivos = 0
        cant_negativos = 0

        for s in resultado1: 

            if s.resultado == True:

                cant_positivos +=1
            
            elif s.resultado == False:

                cant_negativos +=1 

        context['cant_negativosXlocalidad'] = cant_negativos
        context['cant_positivosXlocalidad'] = cant_positivos
        context['TotalLocalidadesFiltrado'] = len(resultado1)
        
    return render(request, 'informe/informeTemplate.html', context)




def ListarAutotest(request):

    context = {}
    todos = Autotest.objects.all()
    context['autotest'] = todos

    return render(request, 'informe/todos.html', context) 


def ListarXLocalidad(request):
    
    context = {}
    localidades = Localidad.objects.all()
    context['localidades'] = localidades


    localidad = request.GET.get("filtro", None)  #retorna el id en string en un queryset
    usuarios = Usuario.objects.filter(localidad= localidad[0])

    resultado1 = []


    for u in usuarios:

        re = Autotest.objects.filter(usuario = u)
        resultado1.append(re[0])

    context['autotest'] = resultado1

    return render(request, 'informe/listarXLocalidad.html', context)




    