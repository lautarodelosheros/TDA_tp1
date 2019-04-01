from maximo import *

def moda(lista):
    diccionario_auxuliar = {}

    for numero in lista:
        diccionario_auxuliar[numero] = diccionario_auxuliar.get(numero, 0) + 1

    lista_valores = list( repetitions.values() )
    el_mas_grande = maximo(values_list)
    repeticion_maxima = 0

    for numero in diccionario_auxuliar:

        if diccionario_auxuliar[numero] == el_mas_grande:
            repeticion_maxima = el_mas_grande
            break

    mensaje = "La moda es: {}".format(repeticion_maxima)
    print(mensaje)
    return repeticion_maxima
