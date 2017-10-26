stringlijst = eval(input("Geef een lijst met minimaal 10 strings: "))
newList = []

for string in stringlijst:
    if len(string) == 4:
        newList.append(string)

print("De gemaakte lijst met alle vier letter strings is: {}".format(newList))
