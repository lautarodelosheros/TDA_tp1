from media import *

def desviacion_estandar(lista):
    media = media(lineList)
    distancia_total = 0

    for numero in lista:
        distancia_local = numero - media
        modulo = (distancia_local) * (distancia_local)
        distancia_total += modulo

    pre_desviacion_estandar = distancia_total / len(lineList)
    return (pre_desviacion_estandar) ** 0.5
