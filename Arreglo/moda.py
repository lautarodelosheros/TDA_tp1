from maximo import maximo

def moda(lista):
    diccionario_auxuliar = {}

    for numero in lista:
        diccionario_auxuliar[numero] = diccionario_auxuliar.get(numero, 0) + 1

    lista_valores = list( diccionario_auxuliar.values() )
    el_mas_grande = maximo(lista_valores)

    for numero in diccionario_auxuliar:

        if diccionario_auxuliar[numero] == el_mas_grande:
            return numero
