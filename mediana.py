def mediana(lineList):
    lista_ordenada = merge_sort(lineList)
    medio = len(lista_ordenada) // 2

    if len(lineList) % 2 == 0:
        numero1 = lista_ordenada[medio]
        numero2 = lista_ordenada[ medio - 1]
        return (numero1 + numero2) / 2

    return lista_ordenada[medio]
