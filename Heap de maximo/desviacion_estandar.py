from media import media

def desviacion_estandar(heap):
    numero_media = media(heap)
    distancia_total = 0

    for numero in heap:
        distancia_local = numero * -1 - numero_media
        modulo = (distancia_local) * (distancia_local)
        distancia_total += modulo

    pre_desviacion_estandar = distancia_total / len(heap)
    return (pre_desviacion_estandar) ** 0.5
