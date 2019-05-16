import sys

def obtenerParametros():
	if (len(sys.argv) != 4):
		raise Exception()
	return [int(sys.argv[1]), sys.argv[2], sys.argv[3]]

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

def cargarJugadores(cantidadJugadores, nombreArchivo, JMR, JPR):	
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

def cargarParejas(nombreArchivo, parejas):	

	archivo = open(nombreArchivo, 'r')
	for pareja in archivo:
		partes = pareja.split(',')
		parejas.append( (partes[0], partes[1].rstrip().strip()) )
def main():

	try:
		parametros = obtenerParametros()
	except:
		print('Faltan parametros, la sintaxis correcta es: Pareo <cantidadJugadores> <archivoJugadores> <archivoParejas>')
		return

	 
	JMR = {}
	JPR = {}	

	parejas = []	

	cargarJugadores(parametros[0], parametros[1], JMR, JPR)
	cargarParejas(parametros[2], parejas)

	for pareja in parejas:
		E = pareja[0]
		
		preferenciasE = JMR[E]
		indicePE = preferenciasE.index(pareja[1])
		
		for i in range(0, indicePE):
			otraPareja = next(filter(lambda pareja: pareja[1] == preferenciasE[i], parejas))
			if(JPR[otraPareja[1]].index(otraPareja[0]) > JPR[otraPareja[1]].index(E)):
				print("ERROR: El matching dado no es estable")
				return

	print("El matching dado es estable")	

	

if __name__ == "__main__":
	main()



