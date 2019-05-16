def media(heap):
    total = 0

    for numero in heap:
        total += numero * -1

    resultado = total / len(heap)

    return resultado
