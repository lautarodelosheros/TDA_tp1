def moda(heap):
    diccionario_auxiliar = {}

    for numero in heap:
        diccionario_auxiliar[numero] = diccionario_auxiliar.get(numero, 0) + 1

    lista_valores = list(diccionario_auxiliar.values())
    el_mas_grande = 0

    for numero in lista_valores:
        if el_mas_grande < numero:
            el_mas_grande = numero

    repeticion_maxima = 0
    resultado = []

    for numero in diccionario_auxiliar:

        if diccionario_auxiliar[numero] == el_mas_grande:
            resultado.append(numero * -1)

    return resultado
