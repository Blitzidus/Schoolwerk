kluizen = open('kluizen.txt', 'r+')
aantal = kluizen.readlines()
kluizen.close()

def toon_aantal_kluizen_vrij():
    ongebruikt = 12 - len(aantal)
    beschikbaar = None
    if ongebruikt <= 0:
        beschikbaar = 'Er zijn geen kluizen beschikbaar'
    else:
        ongebruikt = ('Er zijn {} kluizen beschikbaar'.format(ongebruikt))
        print(ongebruikt)
    return beschikbaar

def nieuwe_kluis():
    kluisnummers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    infile = open('kluizen.txt', 'r+')
    for i in infile.readlines():
        i.split(';')
        i = i[0]
        kluisnummers.remove(i)
    infile.close()
    if len(kluisnummers) > 0 or len(kluisnummers <= 12):
        wachtwoord = input('Voer uw wachtwoord in ')
        if len(wachtwoord) < 4:
            print('Uw wachtwoord moet minimaal 4 tekens bevatten.')
        else:
            outfile = open('kluizen.txt', 'a')
            outfile.write('{}; {}\n'.format(kluisnummers[0], wachtwoord))
            outfile.close()
            return print('U heeft kluisnummer ' + str(kluisnummers[0]))
        return
    else:
        return print('Er zijn helaas geen kluizen meer beschikbaar.')

def kluis_openen():
    kluisID = eval(input('Voer uw kluisnummer in: '))
    kluisWW = input('Voer uw wachtwoord in : ')

    kluizen = open('kluizen.txt', 'r+')
    aantal = kluizen.readlines()
    kluizen.close()

    for i in aantal:
        gesplit = i.split('; ')
        cijfers = int(gesplit[0])
        wachtwoord = gesplit[1].strip('\n')
        if cijfers == kluisID and wachtwoord == kluisWW:
            correct = 'Correct'
            break
        else:
            correct = 'Dat is onjuist'
    return print(correct)


def keuzemenu():
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
    print('2: Ik wil een nieuwe kluis')
    print('3: Ik wil even iets uit mijn kluis halen')
    menu = input()

    if menu == '1':
        toon_aantal_kluizen_vrij()
    elif menu == '2':
        nieuwe_kluis()
    else:
        kluis_openen()

while True:
    keuzemenu()