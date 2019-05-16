from merge_sort import merge_sort

def mediana(lista_enlazada):
    lista_enlazada_ordenada = merge_sort(lista_enlazada)
    medio = lista_enlazada_ordenada.largo() // 2

    if lista_enlazada_ordenada.largo() % 2 == 0:
        numero1 = lista_enlazada_ordenada.obtener(medio)
        numero2 = lista_enlazada_ordenada.obtener( medio - 1 )
        return (numero1 + numero2) / 2

    return lista_enlazada_ordenada.obtener(medio)
