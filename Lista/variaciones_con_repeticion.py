variaciones = []
lista_auxiliar = []

def hacer_variaciones(lista, longitud, posicion):
    for i in range(len(lista)):
        lista_auxiliar[posicion] = lista[i]
        if posicion < (longitud - 1):
            hacer_variaciones(lista, longitud, posicion + 1)
        else:
            variaciones.append(lista_auxiliar[:])

def variaciones_con_repeticion(lista, longitud):
    for i in range(longitud):
        lista_auxiliar.append(0)
    hacer_variaciones(list(set(lista)), longitud, 0)
    return variaciones
