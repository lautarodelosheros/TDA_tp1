# -*- coding: utf-8 -*-

variations = []
list = []

def makeVariations(lineList, r, position):
    for i in range(len(lineList)):
        list[position] = lineList[i]
        if position < (r - 1):
            makeVariations(lineList, r, position + 1)
        else:
            variations.append(list[:])

def variacionesConRepeticion(lineList, r):
    for i in range(int(r)):
        list.append(0)
    makeVariations(lineList, int(r), 0)
    print("Cantidad de variaciones con repetición: ")
    print(str(len(variations)) + "\n")
    print("Lista de variaciones con repetición:\n")
    print(variations)
