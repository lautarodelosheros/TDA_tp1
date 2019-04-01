def maximo(lista):
    el_mas_grande = 0

    for numero in lista:

        if el_mas_grande < numero:
            el_mas_grande = numero

    mensaje = "El maximo es: {}".format(el_mas_grande)
    print(mensaje)
    return el_mas_grande
