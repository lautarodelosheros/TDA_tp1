import heapq
from maximo import maximo
from media import media
from moda import moda
from mediana import mediana
from desviacion_estandar import desviacion_estandar
from permutacion import permutacion
from variaciones_sin_repeticion import variaciones_sin_repeticion
from variaciones_con_repeticion import variaciones_con_repeticion
from generar_archivo_salida import generar_archivo_salida

def ejecutar_funciones(nombre_del_archivo, funcion, lista_parametros):
    resultado = None

    if funcion in ["variaciones_con_repeticion", "variaciones_sin_repeticion"]:

        if len(lista_parametros) > 3:
            longitud_subconjunto = int( lista_parametros[3] )

        else:
            print("Se necesita tercer parámetro para el tamaño del subconjunto")
            exit()

    archivo = open(nombre_del_archivo)
    lista_archivo = [int(linea.rstrip('\n')) * -1 for linea in archivo]
    archivo.close()
    heapq.heapify(lista_archivo)

    try:

        if funcion in ["variaciones_con_repeticion", "variaciones_sin_repeticion"]:
            resultado = obtener_funcion(funcion, True)(lista_archivo, longitud_subconjunto)

        else:
            resultado = obtener_funcion(funcion)(lista_archivo)

    except KeyError:
        print("Función no válida")
        exit()

    """if funcion in locals():
        if funcion in ["variaciones_con_repeticion", "variaciones_sin_repeticion"]:
            resultado = locals()[funcion](lista_archivo, r)
        else:
            resultado = locals()[funcion](lista_archivo)
    else:
        print("Función no válida")"""

    generar_archivo_salida(resultado, funcion)

def obtener_funcion(funcion, extra = False):
    diccionario_variaciones = {"variaciones_sin_repeticion" : variaciones_sin_repeticion,
                               "variaciones_con_repeticion" : variaciones_con_repeticion
                               }

    diccionario_otras_funciones = {"maximo" : maximo,
                                   "media" : media,
                                   "moda" : moda,
                                   "mediana" : mediana,
                                   "desviacion_estandar" : desviacion_estandar,
                                   "permutacion" : permutacion
                                   }

    if extra:
        return diccionario_variaciones[funcion]

    return diccionario_otras_funciones[funcion]
