import sys

def obtenerParametros():
	if (len(sys.argv) != 3):
		raise Exception()
	return [int(sys.argv[1]), sys.argv[2]]

def cargarPreferencias(nombreArchivo):
	listaPreferencias = []

	archivo = open(nombreArchivo, 'r')

	for preferencia in archivo:
		partes = preferencia.split(',')
		listaPreferencias.append( (partes[0], int(partes[1])) )

	#Ordena por prioridad desempatando por posicion en la lista. El primero en aparecer es mejor.
	#Comportamiento por defector de Sort (es estable)
	listaPreferencias.sort(key = lambda elemento: -elemento[1], reverse = True)

	#A partir de ahora solo importa el nombre.
	for i in range(0, len(listaPreferencias)):
		listaPreferencias[i] = listaPreferencias[i][0] 

	return listaPreferencias

def cargarArchivos(cantidadJugadores, nombreArchivo, JMR, JPR):	
	mitadJugadores = cantidadJugadores / 2
	i = 0

	archivo = open(nombreArchivo, 'r')
	for jugador in archivo:
		partes = jugador.split(',')
		
		#Pone la primera mitad en los mejores y la otra en los peores
		if(i < mitadJugadores):
			JMR[partes[1]] = cargarPreferencias(partes[2].rstrip())
		else:
			JPR[partes[1]] = cargarPreferencias(partes[2].rstrip())
		i += 1

def guardarParejas(nombreArchivo, parejas):
	archivo = open(nombreArchivo, 'w')

	for pareja in parejas:
		archivo.write(pareja[1]+", "+pareja[0]+"\n")

def main():

	try:
		parametros = obtenerParametros()
	except:
		print('Faltan parametros, la sintaxis correcta es: Pareo <cantidadJugadores> <archivoJugadores>')
		return

	 
	JMR = {}
	JPR = {}	
	JMRConPareja = []
	parejasArmadas = {}	

	cargarArchivos(parametros[0], parametros[1], JMR, JPR)
	
	JMRLibres = list(JMR.keys())

	while len(JMRLibres):
		JMRElector = JMRLibres.pop()

		PPE = JMR[JMRElector].pop(0)
		parejaPPE = parejasArmadas.get(PPE, False)	
		if(parejaPPE == False):
			parejasArmadas[PPE] = JMRElector
			JMRConPareja.append(JMRElector)
		elif(JPR[PPE].index(JMRElector) < JPR[PPE].index(parejaPPE)):
			JMRLibres.append(parejaPPE)
			parejasArmadas[PPE] = JMRElector
		else:
			JMRLibres.append(JMRElector)


	guardarParejas('Parejas.txt', list(parejasArmadas.items()))

if __name__ == "__main__":
	main()



