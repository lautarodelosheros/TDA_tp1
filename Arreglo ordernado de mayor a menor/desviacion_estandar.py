from media import media

def desviacion_estandar(lista):
    numero_media = media(lista)
    distancia_total = 0

    for numero in lista:
        distancia_local = numero - numero_media
        modulo = (distancia_local) * (distancia_local)
        distancia_total += modulo

    pre_desviacion_estandar = distancia_total / len(lista)
    return (pre_desviacion_estandar) ** 0.5
