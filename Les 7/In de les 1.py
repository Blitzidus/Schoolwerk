def kleinste_veelvoud7(grenswaarde):
    som = 0
    while som < grenswaarde:
        som = som + 7
    return som


resultaat = kleinste_veelvoud7(7000000)
print(resultaat)