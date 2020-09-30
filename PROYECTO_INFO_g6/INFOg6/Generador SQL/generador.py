
from random import *
import time
import os


seed(time.time())
#---------------------------------------------------
# CONSTANTES GLOBALES

CANTIDAD_USERS = 3000    



localidades={'Avia Terai':6203,'Barranqueras':54698,'Barrio de los Pescadores':795,'Basail':1929,'Campo Largo':9069,
			'Capitan Solari':1888,'Charadai':1519,'Charata':26497,'Chorotis':941,'Ciervo Petiso':786,'Colonia Aborigen':1272,
			'Colonia Baranda':336,'Colonia Benitez':2212,'Colonia Elisa':3471,'Colonia Popular':191,'Colonias Unidas':3282,
			'Concepcion del Bermejo':5309,'Coronel Du Graty':7509,'Corzuela':10335,'Cote Lai':1323,'El Espinillo':1261,
			'El Sauzal':715,'El Sauzalito':3374,'Enrique Urien':515,'Estacion General Obligado':31,'Fontana':32027,
			'Fortin las Chunas':302,'Fortin Lavalle':687,'Fuerte Esperanza':1376,'Gancedo':4284,'General Capdevilla':405,
			'General Jose de San Martin':28124,'General Pinedo':13042,'General Vedia':1751,'Haumonia':77,'Hermoso Campo':5011,
			'Horquilla':122,'Ingeniero Barbet':277,'Isla del Cerrito':1758,'Itin':441,'Juan Jose Castelli':27201,'La Clotilde':3382,
			'La Eduvigis':392,'La Escondida':3261,'Laguna Blanca':547,'Laguna Limpia': 1207,'La Leonesa': 8823, 'Lapachito': 888, 
			'La Sabana':242,'Las Breñas':22953,'Las Garcitas':3711,'Las Palmas':4914, 'La Tigra': 2866, 'La Verde': 2717,
			'Los Frentones':5520,'Machagai':21997,'Makalle':4322,'Margarita Belen':5701,'Meson de Fierro':423,'Miraflores':4737,
			'Napalpi':39,'Napenay':2661,'Nueva Pompeya':2259,'Pampa Almiron':1278,'Pampa del Indio':9204,'Pampa del Infierno':9063,
			'Pampa Landriel':333,'Presidencia del Plaza':9642,'Presidencia Roca':4201,'Presidencia Roque Saenz Peña':89882,
			'Puerto Bermejo Nuevo':1733,'Puerto Bermejo Viejo':86,'Puerto Eva Peron':609,'Puerto Tirol':8819,'Puerto Vilelas':8278,
			'Quitilipi':24517,'Resistencia':290723,'Rio Muerto':1052,'Samuhu':1251,'San Bernardo':9379,'Santa Sylvina':7340,
			'Selva del Rio de Oro':606,'Taco Pozo':7813,'Tres Isletas':16976,'Venados Grandes':303,'Villa Angela':41403,
			'Villa Berthet':10224,'Villa El Palmar':879,'Villa Rio Bermejito':3752,'Wichi':773,'Zaparinqui':700}

apellidos =['Alfonzo', 'Aguirre', 'Azul', 'González','Rodríguez','Gómez','Fernández','López','Díaz','Martínez','Pérez','García','Sánchez',
			'Romero','Sosa','Torres','Álvarez','Ruiz','Ramírez','Flores','Benítez','Acosta','Medina','Herrera','Suárez','Aguirre','Giménez',
			'Gutiérrez','Pereyra','Rojas','Molina','Castro','Ortiz','Silva','Núñez','Luna','Juárez','Cabrera','Ríos','Morales','Godoy','Moreno',
			'Ferreyra','Domínguez','Carrizo','Peralta','Castillo','Ledesma','Quiroga','Vega','Vera','Muñoz','Ojeda','Ponce','Villalba','Cardozo',
			'Navarro','Coronel','Vázquez','Ramos','Vargas','Cáceres','Arias','Figueroa','Córdoba','Correa']

nombres =  ['Isabella','Martina','Catalina','Sofia','Olivia','Emma','Delfina','Francesca','Valentina','Emilia','Martha','Roxana','Ana María',
			'Elizabeth','Sonia','Juana','Patricia','Lidia','Rosmery','Carmen','Laura','Ana Patricia','Lucía','Paula','Silvia','María','Benjamin',
			'Bautista','Felipe','Valentino','Benicio','Joaquin','Lorenzo','Mateo','Santino','Juan','Ignacio','Juan Carlos','Marco Antonio',
			'Miguel Ángel','Juan','Mario','David','Fernando','Víctor Hugo','Jorge','Hugo','Antonio','Pablo','Mario','José Manuel','Víctor'] 


def generadorLocalidades():

	for loc in localidades.items():

		values = "('"+loc[0]+"',"+str(loc[1])+')'
		linea = "INSERT INTO users_localidad (nombre,cant_habitantes) VALUES "+values
		print(linea+"\n")
		file.write(linea+os.linesep)
		
		

def validarAutotest(u):
	
	contador = 0
	for s in u:
		if bool(s): 
			contador += 1

		if contador>3:
			return True

	return False
	

def generadorSolicitud(u):

	usuario_id = u
	autotest_id = u
	dia = randint(1, 28)
	mes = randint(7,9)
	fecha_creacion ="'"+str(mes)+'-'+str(dia)+'-2020'+"'"
	fecha_hisopado = "'"+str(mes)+'-'+str(dia+2)+'-2020'+"'"
	estado = str(3) # 1: Pendiente de hisopar 2: Hisopado pendiente de resultados 3: resultados
	resultado = str(randint(0,1))
	values = '('+usuario_id+','+autotest_id+','+fecha_creacion+','+fecha_hisopado+','+estado+','+resultado+')'
	linea = "INSERT INTO Autotest_solicitud (usuario_id,autotest_id,fecha_creacion, fecha_hisopado,estado, resultado ) VALUES "+values
	print(linea+"\n")
	file.write(linea+os.linesep)
	

idusuario=1

def generadorAutotestsSolicitudes(idusuario):

	usuario_id = idusuario
	tosSeca= str(randint(0,1))
	fiebre = str(randint(0,1))
	dolordeGarganta = str(randint(0,1))
	dolorCorporal = str(randint(0,1))
	contactoConPositivo = str(randint(0,1))
	dolorCabeza = str(randint(0,1))
	dificultadRespiratoria = str(randint(0,1))
	alteracionGustoOfalto = str(randint(0,1))
	mucosidad = str(randint(0,1))
	enfermedad = str(randint(0,1))
	vomitos = str(randint(0,1))
	diarrea = str(randint(0,1))
	u = [usuario_id,tosSeca,fiebre,dolordeGarganta,dolorCorporal,contactoConPositivo,dolorCabeza,dificultadRespiratoria,alteracionGustoOfalto,mucosidad,enfermedad,vomitos,diarrea]
	corresponde_hisopado = str(int(validarAutotest(u)))
	values = '('+u[0]+','+u[1]+','+u[2]+','+u[3]+','+u[4]+','+u[5]+','+u[6]+','+u[7]+','+u[8]+','+u[9]+','+u[10]+','+u[11]+','+u[12]+','+corresponde_hisopado+')'
	linea = "INSERT INTO Autotest_autotest (usuario_id,tosSeca,fiebre,dolordeGarganta,dolorCorporal,contactoConPositivo,dolorCabeza,dificultadRespiratoria,alteracionGustoOfalto,mucosidad,enfermedad,vomitos,diarrea,corresponde_hisopado) VALUES "+values
	print(linea+"\n")
	file.write(linea+os.linesep)
	
	if validarAutotest(u):

		generadorSolicitud(idusuario)


def generadorUsuarios():

	
	num_id = 0

	for user in range(1, CANTIDAD_USERS+1):

		nom = nombres[randint(0,len(nombres)-1)]
		ape = apellidos[randint(0,len(apellidos)-1)]
		email = "'"+nom+'_'+ape+'@gmail.com.ar'+"'"
		username="'"+nom+'_'+ape+"'"
		telefono = str(15000000 + randint(111111,999999))
		dni =str(randint(111111,99999999))
		id_localidad = str(randint(1,len(localidades)-1))
		domicilio="'"+'Av Cualquiera 123'+"'"
		nom = "'"+nom+"'"
		ape = "'"+ape+"'"
		pas = "'Inst45wall'"
		superuser= str(0)
		staff=str(0)
		active=str(0)
		datej = "'"+str(randint(7,9))+"/"+str(randint(1,28))+"/"+str(2020)+"'"
		dateb = "'"+str(randint(1,12))+"/"+str(randint(1,28))+"/"+str(randint(1935,2010))+"'"
		num_id +=1
		values = '('+email+','+telefono+','+domicilio+','+dni+','+nom+','+ape+','+id_localidad+','+pas+','+superuser+','+username+','+staff+','+active+','+datej+','+dateb+')'
		linea = "INSERT INTO users_usuario (email,telefono,domicilio,dni,first_name,last_name,localidad_id,password,is_superuser,username,is_staff,is_active,date_joined,fecha_nac) VALUES"+values
		print(linea+"\n")
		file.write(linea+os.linesep)

		generadorAutotestsSolicitudes(str(num_id))

	


# Ejecucion------------------------------------------------------

RUTA= "C:/Users/Gonzalo/Desktop/script-info.txt"  # Ruta de creacion del Script

file = open(RUTA, "w")


generadorLocalidades()
generadorUsuarios()


file.close()