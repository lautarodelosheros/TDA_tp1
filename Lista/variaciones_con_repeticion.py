variaciones = []
lista_auxiliar = []

def hacer_variaciones(lista_enlazada, longitud_subconjunto, posicion):

    for i in range(lista_enlazada.largo()):
        lista_auxiliar[posicion] = lista_enlazada.obtener(i)

        if posicion < (longitud_subconjunto - 1):
            hacer_variaciones(lista_enlazada, longitud_subconjunto, posicion + 1)

        else:
            variaciones.append(lista_auxiliar[ : ])

def variaciones_con_repeticion(lista_enlazada, longitud_subconjunto):

    for i in range(longitud_subconjunto):
        lista_auxiliar.append(0)

    hacer_variaciones(lista_enlazada, longitud_subconjunto, 0)
    return variaciones
