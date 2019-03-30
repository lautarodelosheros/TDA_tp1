#!/usr/bin/env python3
import sys
from maximo import maximo
from media import media
from moda import moda

fileName = sys.argv[1]
function = sys.argv[2]

lineList = [line.rstrip('\n') for line in open(fileName)]

if function in locals():
    locals()[function](lineList)
else:
    print("Funcion no valida")
