def permutaciones(heap, longitud):
    resultado = []

    if longitud == 1:
        for numero in heap:
            resultado.append([numero * -1])
        return resultado
    else:
        for numero in heap:
            for permutacion in permutaciones(list(set(heap) - set([numero * -1])), longitud - 1):
                resultado.append([numero * -1] + permutacion)

        return resultado

def variaciones_sin_repeticion(heap, longitud):
    return permutaciones(heap, longitud)
