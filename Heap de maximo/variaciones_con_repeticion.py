variaciones = []
lista_auxiliar = []

def hacer_variaciones(heap, longitud, posicion):
    for i in range(len(heap)):
        lista_auxiliar[posicion] = heap[i] * -1
        if posicion < (longitud - 1):
            hacer_variaciones(heap, longitud, posicion + 1)
        else:
            variaciones.append(lista_auxiliar[:])

def variaciones_con_repeticion(heap, longitud):
    for i in range(longitud):
        lista_auxiliar.append(0)
    hacer_variaciones(heap, longitud, 0)
    return variaciones
