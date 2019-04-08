from merge_sort import merge_sort

def mediana(lista):
    lista_ordenada = merge_sort(lista)
    medio = len(lista_ordenada) // 2

    if len(lista_ordenada) % 2 == 0:
        numero1 = lista_ordenada[medio]
        numero2 = lista_ordenada[ medio - 1]
        return (numero1 + numero2) / 2

    return lista_ordenada[medio]
