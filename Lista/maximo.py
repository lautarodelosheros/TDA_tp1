def maximo(lista):

    if len(lista) == 0:
        raise ValueError("La lista está vacia")

    el_mas_grande = lista[0]

    for numero in lista:

        if el_mas_grande < numero:
            el_mas_grande = numero

    return el_mas_grande
