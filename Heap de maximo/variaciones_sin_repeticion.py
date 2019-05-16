def permutaciones(heap, longitud_subconjunto):
    resultado = []

    if longitud_subconjunto == 1:

        for numero in heap:
            resultado.append([numero * -1])
            
        return resultado

    else:

        for numero in heap:

            for permutacion in permutaciones(list(set(heap) - set([numero])), longitud_subconjunto - 1):
                resultado.append([numero * -1] + permutacion)

        return resultado

def variaciones_sin_repeticion(heap, longitud_subconjunto):
    return permutaciones(heap, longitud_subconjunto)
