from lista_enlazada import *

def merge_sort(lista_enlazada):

    if lista_enlazada.largo() < 2:
        return lista_enlazada

    medio = lista_enlazada.largo() // 2
    izquierda = merge_sort( lista_enlazada.slice(0, medio) )
    derecha = merge_sort( lista_enlazada.slice(medio) )
    return merge(izquierda, derecha)

def merge(lista_enlazada1, lista_enlazada2):
    i, j = 0, 0
    resultado = ListaEnlazada()

    while ( i < lista_enlazada1.largo() ) and ( j < lista_enlazada2.largo() ):
        valor1 = lista_enlazada1.obtener(i)
        valor2 = lista_enlazada2.obtener(j)

        if valor1 < valor2:
            resultado.insertar_ultimo(valor1)
            i += 1

        else:
            resultado.insertar_ultimo(valor2)
            j += 1

    resultado += lista_enlazada1.slice(i)
    resultado += lista_enlazada2.slice(j)

    return resultado
