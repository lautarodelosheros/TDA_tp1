def generar_archivo_salida(resultado_obtenido, funcion):
    with open("resultado.txt", "w") as archivo_salida:

        if type(resultado_obtenido) is int or type(resultado_obtenido) is float:
            archivo_salida.write("El resultado obtenido de {} es: {}\n".format(funcion, resultado_obtenido) )
            return

        archivo_salida.write("El resultado obtenido de {} es: \n".format(funcion) )    

        for subconjunto in resultado_obtenido:
            archivo_salida.write("{}\n".format(tuple(subconjunto)) )
