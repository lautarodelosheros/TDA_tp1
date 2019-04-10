#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from ejecutar_funciones import ejecutar_funciones

def main():

    if len(sys.argv) > 2:
        nombre_del_archivo = sys.argv[1]
        funcion = sys.argv[2]
        ejecutar_funciones(nombre_del_archivo, funcion, sys.argv)

    else:
        print("Se necesitan al menos dos parámetros")
        exit()

main()
