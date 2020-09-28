from django.shortcuts import render

# Create your views here.

from apps.Autotest.models import Autotest, Solicitud
from apps.users.models import Localidad, Usuario





def Informe(request):

    context={}
    context['total_autotest'] = Autotest.objects.count()
    total_solicitud = Solicitud.objects.count()
    context['total_solicitud'] = total_solicitud
    context['tosSeca'] = Autotest.objects.filter(tosSeca=True).count()
    context['fiebre'] = Autotest.objects.filter(fiebre=True).count()
    context['dolordeGarganta'] = Autotest.objects.filter(dolordeGarganta=True).count()
    context['dolorCorporal'] = Autotest.objects.filter(dolorCorporal=True).count()
    context['contactoConPositivo'] = Autotest.objects.filter(contactoConPositivo=True).count()
    context['dolorCabeza'] = Autotest.objects.filter(dolorCabeza=True).count()
    context['dificultadRespiratoria'] = Autotest.objects.filter(dificultadRespiratoria=True).count()
    context['alteracionGustoOfalto'] =Autotest.objects.filter(alteracionGustoOfalto=True).count()
    context['mucosidad'] = Autotest.objects.filter(mucosidad=True).count()
    context['enfermedad'] = Autotest.objects.filter(enfermedad=True).count()
    context['vomitos'] = Autotest.objects.filter(vomitos=True).count()
    context['diarrea'] = Autotest.objects.filter(tosSeca=True).count()
    total_positivos = Solicitud.objects.filter(resultado=True).count()
    context['total_positivos'] = total_positivos
    total_negativos = Solicitud.objects.filter(resultado=False).count()
    context['total_negativos'] = total_negativos
 
    

    context['porcentajeTotalPositivos'] = round((total_positivos/total_solicitud)*100)    
    context['porcentajeTotalNegativos'] = round((total_negativos/total_solicitud)*100)

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


        # TOTALIZADORES PARA POSITIVOS Y NEGATIVOS FILTRADO LOCALIDAD
        cant_positivosXlocalidad = 0
        cant_negativosXlocalidad = 0

        for s in resultado1: 

            if s.resultado == True:

                cant_positivosXlocalidad +=1
            
            elif s.resultado == False:

                cant_negativosXlocalidad +=1 

        # TOTALIZADORES PARA SINTOMAS FILTRADOS X LOCALIDAD
        total_tosSecaXlocalidad = 0
        total_fiebreXlocalidad = 0
        total_dolordeGargantaXlocalidad = 0
        total_dolorCorporalXlocalidad = 0
        total_contactoConPositivoXlocalidad = 0
        total_dolorCabezaXlocalidad = 0
        total_dificultadRespiratoriaXlocalidad = 0
        total_alteracionGustoOfaltoXlocalidad = 0
        total_mucosidadXlocalidad = 0
        total_enfermedadXlocalidad = 0
        total_vomitosXlocalidad = 0
        total_diarreaXlocalidad = 0


        for r in resultado2:

            if r.tosSeca:
                total_tosSecaXlocalidad +=1  
            if r.fiebre:
                total_fiebreXlocalidad +=1
            if r.dolordeGarganta:
                total_dolordeGargantaXlocalidad +=1
            if r.dolorCorporal:
                total_dolorCorporalXlocalidad +=1
            if r.contactoConPositivo:
                total_contactoConPositivoXlocalidad +=1
            if r.dolorCabeza:
                total_dolorCabezaXlocalidad +=1
            if r.dificultadRespiratoria:
                total_dificultadRespiratoriaXlocalidad +=1
            if r.alteracionGustoOfalto:
                total_alteracionGustoOfaltoXlocalidad +=1
            if r.mucosidad:
                total_mucosidadXlocalidad +=1
            if r.enfermedad:
                total_enfermedadXlocalidad +=1
            if r.vomitos:
                total_vomitosXlocalidad +=1
            if r.diarrea:
                total_diarreaXlocalidad +=1

        context['total_tosSecaXlocalidad'] = round((total_tosSecaXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)
        context['total_fiebreXlocalidad'] = round((total_fiebreXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)
        context['total_dolordeGargantaXlocalidad'] = round((total_dolordeGargantaXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)
        context['total_dolorCorporalXlocalidad'] = round((total_dolorCorporalXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)
        context['total_contactoConPositivoXlocalidad'] = round((total_contactoConPositivoXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)
        context['total_dolorCabezaXlocalidad'] = round((total_dolorCabezaXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)
        context['total_dificultadRespiratoriaXlocalidad'] = round((total_dificultadRespiratoriaXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)
        context['total_alteracionGustoOfaltoXlocalidad'] = round((total_alteracionGustoOfaltoXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)
        context['total_mucosidadXlocalidad'] = round((total_mucosidadXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)
        context['total_enfermedadXlocalidad'] = round((total_enfermedadXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)
        context['total_vomitosXlocalidad'] = round((total_vomitosXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)
        context['total_diarreaXlocalidad'] = round((total_diarreaXlocalidad/(cant_positivosXlocalidad+cant_negativosXlocalidad))*100)


        

        context['cant_negativosXlocalidad'] = cant_negativosXlocalidad
        context['cant_positivosXlocalidad'] = cant_positivosXlocalidad
        context['TotalSolicitudesLocalidadesFiltrado'] = len(resultado1)
        context['TotalAutotestsLocalidadesFiltrado'] = len(resultado2)


        context['porcentajePositivoXlocalidad'] = round((cant_positivosXlocalidad / len(resultado1))*100)
        context['porcentajeNegativoXlocalidad'] = round((cant_negativosXlocalidad / len(resultado1))*100)
        
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




    