def moda(lineList):
    dict = {}
    for number in lineList:
        if number in dict:
            dict[number] = dict[number] + 1
        else:
            dict[number] = 1
    max = ""
    for number in dict:
        if dict.get(max) < dict.get(number):
            max = number
    print("La moda es " + max)
