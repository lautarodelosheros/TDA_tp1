def mediana(lista):

    medio = len(lista_ordenada) // 2

    if len(lista) % 2 == 0:
        numero1 = lista[medio]
        numero2 = lista[medio - 1]
        mediana = (numero1 + numero2) / 2.0
    else:
        mediana = lista[medio]

    return mediana
