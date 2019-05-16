from lista_enlazada import *

def permutaciones(lista_enlazada, longitud_subconjunto):
    resultado = ListaEnlazada()

    if longitud_subconjunto == 1:

        for numero in lista_enlazada:
            lista_auxiliar = ListaEnlazada()
            lista_auxiliar.insertar_ultimo(numero)
            resultado.insertar_ultimo(lista_auxiliar)
        return resultado

    else:

        for numero in lista_enlazada:
            conjunto1 = set(lista_enlazada)
            conjunto2 = set([numero])
            conjunto3 = conjunto1 - conjunto2
            lista_auxiliar = convertir_a_lista_enlazada(conjunto3)

            for permutacion in permutaciones(lista_auxiliar, longitud_subconjunto - 1):
                lista = ListaEnlazada()
                lista.insertar_ultimo(numero)
                resultado.insertar_ultimo(lista + permutacion)

        return resultado

def variaciones_sin_repeticion(lista_enlazada, longitud_subconjunto):
    return permutaciones(lista_enlazada, longitud_subconjunto)

def convertir_a_lista_enlazada(iterable):
    lista_enlazada = ListaEnlazada()

    for elemento in iterable:
        lista_enlazada.insertar_ultimo(elemento)

    return lista_enlazada
"""result = []

def printCombination(arr, n, r):

    # A temporary array to
    # store all combination
    # one by one
    data = [0]*r;

    # Print all combination
    # using temprary array 'data[]'
    return combinationUtil(arr, data, 0,
                    n - 1, 0, r);

# arr[] ---> Input Array
# data[] ---> Temporary array to
#         store current combination
# start & end ---> Staring and Ending
#             indexes in arr[]
# index ---> Current index in data[]
# r ---> Size of a combination
# to be printed
def combinationUtil(arr, data, start,
                    end, index, r):

    # Current combination is ready
    # to be printed, print it
    if (index == r):
        copy = data[:];
        result.append(copy);
        return;

    # replace index with all
    # possible elements. The
    # condition "end-i+1 >=
    # r-index" makes sure that
    # including one element at
    # index will make a combination
    # with remaining elements at
    # remaining positions
    i = start;
    while(i <= end and end - i + 1 >= r - index):
        data[index] = arr[i];
        combinationUtil(arr, data, i + 1,
                        end, index + 1, r);
        i += 1;
"""
