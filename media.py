def media(lista):
    total = 0

    for numero in lista:
        total += numero

    resultado = total / len(lista)
    mensaje = "La media es: {}".format(resultado)
    print(mensaje)

    return resultado
