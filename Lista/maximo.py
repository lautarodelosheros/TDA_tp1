def maximo(lista_enlazada):

    if lista_enlazada.largo() == 0:
        raise ValueError("La lista está vacia")

    el_mas_grande = lista_enlazada.ver_primero()

    for numero in lista_enlazada:

        if el_mas_grande < numero:
            el_mas_grande = numero

    return el_mas_grande
