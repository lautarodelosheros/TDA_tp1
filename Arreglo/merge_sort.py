def merge_sort(lista):

    if len(lista) < 2:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[ : medio])
    derecha = merge_sort(lista[medio : ])
    return merge(izquierda, derecha)

def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []

    while (i < len(lista1) and j < len(lista2) ) :

        if lista1[i] < lista2[j]:
            resultado.append( lista1[i] )
            i += 1

        else:
            resultado.append( lista2[j] )
            j += 1

    resultado += lista1[ i : ]
    resultado += lista2[ j : ]

    return resultado
