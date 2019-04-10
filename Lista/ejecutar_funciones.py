from maximo import maximo
from media import media
from moda import moda
from mediana import mediana
from desviacion_estandar import desviacion_estandar
from permutacion import permutacion
from variaciones_sin_repeticion import variaciones_sin_repeticion
from variaciones_con_repeticion import variaciones_con_repeticion
from generar_archivo_salida import generar_archivo_salida
from lista_enlazada import *

def ejecutar_funciones(nombre_del_archivo, funcion, lista_parametros):
    resultado = None

    if funcion in ["variaciones_con_repeticion", "variaciones_sin_repeticion"]:

        if len(lista_parametros) > 3:
            longitud_subconjunto = int( lista_parametros[3] )

        else:
            print("Se necesita tercer parámetro para el tamaño del subconjunto")
            exit()

    lista_archivo = ListaEnlazada()
    with open(nombre_del_archivo) as archivo_entrada:

        for linea in archivo_entrada:
            lista_archivo.insertar_ultimo( int( linea.rstrip('\n') ) )

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
                                   "mediana" : mediana,
                                   "moda" : moda,
                                   "desviacion_estandar" : desviacion_estandar,
                                   "permutacion" : permutacion
                                   }

    if extra:
        return diccionario_variaciones[funcion]

    return diccionario_otras_funciones[funcion]
