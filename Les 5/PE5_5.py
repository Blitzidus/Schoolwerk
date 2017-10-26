def gemiddelde(string):
    list = string.split(" ")
    totalLenght = 0
    for word in list:
        totalLenght += len(word)
    middleLenght = round(totalLenght / len(list))
    return "Uw gemiddelde woord lengte is: {}".format(middleLenght)


while True:
    print(gemiddelde(input("Geef een zin op: ")))
