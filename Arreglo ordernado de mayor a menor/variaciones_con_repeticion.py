variaciones = []
lista_auxiliar = []

def hacer_variaciones(lista, longitud_subconjunto, posicion):

    for i in range(len(lista)):
        lista_auxiliar[posicion] = lista[i]

        if posicion < (longitud_subconjunto - 1):
            hacer_variaciones(lista, longitud_subconjunto, posicion + 1)

        else:
            variaciones.append(lista_auxiliar[:])

def variaciones_con_repeticion(lista, longitud_subconjunto):

    for i in range(longitud_subconjunto):
        lista_auxiliar.append(0)

    hacer_variaciones(lista, longitud_subconjunto, 0)
    return variaciones
