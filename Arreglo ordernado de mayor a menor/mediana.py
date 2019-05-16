def mediana(lista):
    medio = len(lista) // 2
    lista.reverse()

    if len(lista) % 2 == 0:
        numero1 = lista[medio]
        numero2 = lista[medio - 1]
        return (numero1 + numero2) / 2

    return lista[medio]
