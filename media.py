def media(lineList):
    total = 0
    for number in lineList:
        total = total + int(number)
    print("La media es: " + str(total / len(lineList)))
    return
