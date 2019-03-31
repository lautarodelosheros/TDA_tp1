#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from maximo import maximo
from media import media
from moda import moda
from variacionesConRepeticion import variacionesConRepeticion

if len(sys.argv) > 2:
    fileName = sys.argv[1]
    function = sys.argv[2]
    if function == 'variacionesConRepeticion':
        if len(sys.argv) > 3:
            r = sys.argv[3]
        else:
            print("Se necesita tercer parámetro para el tamaño del subconjunto")
            exit()
else:
    print("Se necesitan al menos dos parámetros")
    exit()

lineList = [line.rstrip('\n') for line in open(fileName)]

if function in locals():
    if function == 'variacionesConRepeticion':
        locals()[function](lineList, r)
    else:
        locals()[function](lineList)
else:
    print("Función no válida")
