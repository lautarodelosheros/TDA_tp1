def moda(lista):
    diccionario_auxiliar = {}

    for numero in lista:
        diccionario_auxiliar[numero] = diccionario_auxiliar.get(numero, 0) + 1

    lista_valores = list(diccionario_auxiliar.values())
    el_mas_grande = lista_valores[0]

    for numero in lista_valores:

        if el_mas_grande < numero:
            el_mas_grande = numero

    for numero in diccionario_auxiliar:

        if diccionario_auxiliar[numero] == el_mas_grande:
            return numero
