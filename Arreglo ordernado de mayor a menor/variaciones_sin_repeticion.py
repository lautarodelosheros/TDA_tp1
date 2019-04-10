def permutaciones(lista, longitud_subconjunto):
    resultado = []

    if longitud_subconjunto == 1:

        for numero in lista:
            resultado.append([numero])
        return resultado

    else:

        for numero in lista:

            for permutacion in permutaciones(list(set(lista) - set([numero])), longitud_subconjunto - 1):
                resultado.append([numero] + permutacion)

        return resultado

def variaciones_sin_repeticion(lista, longitud_subconjunto):
    return permutaciones(lista, longitud_subconjunto)
