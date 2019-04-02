from maximo import *

def moda(lista):
    diccionario_auxiliar = {}

    for numero in lista:
        diccionario_auxiliar[numero] = diccionario_auxiliar.get(numero, 0) + 1

    lista_valores = list(diccionario_auxiliar.values())
    el_mas_grande = maximo(lista_valores)
    repeticion_maxima = 0
    resultado = []

    for numero in diccionario_auxiliar:

        if diccionario_auxiliar[numero] == el_mas_grande:
            resultado.append(numero)

    return resultado
