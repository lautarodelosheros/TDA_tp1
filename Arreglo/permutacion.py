def permutacion(lista):

    if len(lista) == 0:
        return []

    if len(lista) == 1:
        return [lista]

    resultado = []

    for i in range(len(lista)):
       dato = lista[i]
       lista_remanente = lista[ : i] + lista[ i + 1 : ]

       for elemento in permutacion(lista_remanente):
           resultado.append([dato] + elemento)

    return resultado

"""
resultado = []

def permutacion(lista, tamanio):

    if tamanio == 1:
        lista_copia = lista[ : ]
        resultado.append(lista_copia)

    for i in range(tamanio):
        permutacion(lista, tamanio - 1)

        if tamanio % 2 == 1:
            lista[0], lista[tamanio - 1] = lista[tamanio - 1], lista[0]

        else:
            lista[i], lista[tamanio - 1] = lista[tamanio - 1], lista[i]
"""
