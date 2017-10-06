cijfers = [8, 7, 8, 9, 10, 7, 6]
resultaten = ()
for cijfer in cijfers:
    if cijfer in resultaten:
        resultaten(cijfer) = resultaten(cijfer) + 1
    else:
        resultaten(cijfer) = 1

print(resultaten)