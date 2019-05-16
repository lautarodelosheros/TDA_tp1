from media import media

def desviacion_estandar(lista_enlazada):
    numero_media = media(lista_enlazada)
    distancia_total = 0

    for numero in lista_enlazada:
        distancia_local = numero - numero_media
        modulo = (distancia_local) * (distancia_local)
        distancia_total += modulo

    pre_desviacion_estandar = distancia_total / lista_enlazada.largo()
    return (pre_desviacion_estandar) ** 0.5
