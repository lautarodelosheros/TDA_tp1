def maximo(lineList):
    max = 0
    for number in lineList:
        if max < number:
            max = number
    print("El maximo es: " + max)
    return
