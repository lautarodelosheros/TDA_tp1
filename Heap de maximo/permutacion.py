def permutacion(heap):

    if len(heap) == 0:
        return []

    if len(heap) == 1:
        return [heap * -1]

    resultado = []

    for i in range(len(heap)):
       dato = heap[i]
       lista_remanente = heap[ : i] + heap[ i + 1 : ]

       for elemento in permutacion(lista_remanente):
           resultado.append([dato * -1] + elemento)

    return resultado
