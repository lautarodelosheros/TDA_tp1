def media(lista_enlazada):
    total = 0

    for numero in lista_enlazada:
        total += numero

    resultado = total / lista_enlazada.largo()

    return resultado
