def kwadraten_som(grondgetallen):
    result = 0
    for i in grondgetallen:
        if i >= 0:
            result = result + i**2

    return result
print(kwadraten_som((4, 5, 3, -81)))

