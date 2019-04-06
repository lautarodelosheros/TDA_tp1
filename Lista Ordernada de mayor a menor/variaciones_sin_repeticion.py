def permutaciones(lista, longitud):
    resultado = []

    if longitud == 1:
        for numero in lista:
            resultado.append([numero])
        return resultado
    else:
        for numero in lista:
            for permutacion in permutaciones(list(set(lista) - set([numero])), longitud - 1):
                resultado.append([numero] + permutacion)

        return resultado

def variaciones_sin_repeticion(lista, longitud):
    return permutaciones(lista, longitud)
