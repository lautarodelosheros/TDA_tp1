from lista_enlazada import *

def permutacion(lista_enlazada):

    if lista_enlazada.largo() == 0:
        return ListaEnlazada()

    if lista_enlazada.largo() == 1:
        lista = ListaEnlazada()
        lista.insertar_ultimo(lista_enlazada)
        return lista

    resultado = ListaEnlazada()

    for i in range( lista_enlazada.largo() ):
       dato = lista_enlazada.obtener(i)
       lista_remanente = lista_enlazada.slice(0, i) + lista_enlazada.slice(i + 1)

       for elemento in permutacion(lista_remanente):
           lista = ListaEnlazada()
           lista.insertar_ultimo(dato)
           resultado.insertar_ultimo(lista + elemento)

    return resultado

"""resultado = []

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
