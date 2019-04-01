def permutacion(lista): 

    if len(lista) == 0:
        return []

    if len(lista) == 1:
        return [lista]

    resultado = []

    for i in range(len(lista)):
       dato = lista[i]
       lista_remanente = lista[ : i] + lista[ i + 1 : ]

       for elemento in permutation(lista_remanente):
           resultado.append([dato] + elemento)

    return resultado
