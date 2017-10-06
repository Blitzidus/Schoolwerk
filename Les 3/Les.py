nameAgeList = [('Jeroen', 18), ('Pieter' , 14), ('Maria', 23)]

#name = input('geef je naam: ')
#age = eval(input('Geef je leeftijd: '))
for item in nameAgeList:
    name = item[0]
    age = item[1]
    if age >= 18:
        print('Beste ' + name + ', je mag stemmen.')
    else:
        wachtTijd = 18 - age
        print('Beste ' + name + ', je moet nog ' + str(wachtTijd) + ' jaar wachten.')

print('klaar')