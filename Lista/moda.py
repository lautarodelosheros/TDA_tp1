from maximo import maximo
from variaciones_sin_repeticion import convertir_a_lista_enlazada
from lista_enlazada import *

def moda(lista_enlazada):
    diccionario_auxuliar = {}

    for numero in lista_enlazada:
        diccionario_auxuliar[numero] = diccionario_auxuliar.get(numero, 0) + 1

    lista_valores = convertir_a_lista_enlazada( diccionario_auxuliar.values() )
    el_mas_grande = maximo(lista_valores)
    repeticion_maxima = 0

    for numero in diccionario_auxuliar:

        if diccionario_auxuliar[numero] == el_mas_grande:
            repeticion_maxima = el_mas_grande
            break

    return repeticion_maxima
