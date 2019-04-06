#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from maximo import maximo
from media import media
from moda import moda
from mediana import mediana
from desviacion_estandar import desviacion_estandar
from permutacion import permutacion
from variaciones_con_repeticion import variaciones_con_repeticion
from variaciones_sin_repeticion import variaciones_sin_repeticion

if len(sys.argv) > 2:
    nombre_archivo = sys.argv[1]
    funcion = sys.argv[2]
    if funcion in ['variaciones_con_repeticion', 'variaciones_sin_repeticion']:
        if len(sys.argv) > 3:
            longitud_subconjunto = sys.argv[3]
        else:
            print("Se necesita tercer parámetro para el tamaño del subconjunto")
            exit()
else:
    print("Se necesitan al menos dos parámetros")
    exit()

lista = [int(line.rstrip('\n')) for line in open(nombre_archivo)]

if funcion in locals():
    if funcion in ['variaciones_con_repeticion', 'variaciones_sin_repeticion']:
        variaciones = locals()[funcion](lista, int(longitud_subconjunto))
        print("Cantidad de variaciones: ")
        print(str(len(variaciones)) + "\n")
        print("Lista de variaciones:\n")
        print(variaciones)
    else:
        resultado = locals()[funcion](lista)
        mensaje = "{} es: {}".format(funcion, resultado)
        print(mensaje)
else:
    print("Función no válida")
