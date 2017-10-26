import random
import csv


def Nieuwe_Fiets_Registreren():
    'User has new bike'
    naam = input('Wat is uw naam?')
    nummer = str(random.randrange(0, 999))  # random nummer
    infile = open('nummers.txt', 'r')  # Read file
    nummer_persoon_wachtwoord = infile.read()  # file toekennen aan variable
    if nummer in nummer_persoon_wachtwoord:  # als random nummer al in het file zit
        nummer = random.randrange(0, 999)  # zo ja, nieuw nummer
    else:
        infile.close()  # anders ff file sluiten
        wachtwoord = input('Wat wordt uw wachtwoord?')
        if len(wachtwoord) <= 8:  # wachtwoord langer dan 8 aub
            print('Uw wachtwoord moet langer dan 8 karakters zijn')
            wachtwoord = input('Wat wordt uw wachtwoord?')
        elif len(wachtwoord) > 8:
            print('Bedankt voor het registreren!')
            print('U heeft nummer: {}'.format(nummer))
            outfile = open('nummers.txt', 'a')
            outfile.write('{},{},{},{}\n'.format(nummer, naam, wachtwoord, strtime()))  # schrijven ff alles in de file
            outfile.close()
            print()
            print()
            return opties()


def strtime():
    import datetime
    vandaag = datetime.datetime.today()
    tijd = vandaag.strftime("%a %d %b %Y %I:%M %p")
    return tijd


def Fiets_Stallen():
    'User wants to store bike'
    with open('datalijst.csv', 'w', newline ='') as csvfile:
        writer = scv.writer(csvfile, delimiter=' ')
        write.writerow((('{};{};{};{};{};\n'.format(strtime(), fietsnummer(), naam()))
        naam = input('Wat is uw naam?')
        wachtwoord = input('Wat is uw wachtwoord?')
        infile = open('nummers.txt', 'r')
        naam_persoon_wachtwoord = infile.read()
        if naam not in naam_persoon_wachtwoord:
            print('Uw fietsnummer is incorrect.')
            print('1: Opnieuw proberen')
            print('2: Terug naar startscherm')
            keuze = eval(input('Kies uw optie'))
            if keuze == 1:
                opties()
            elif keuze == 2:
                Fiets_Stallen()
        else:



def Fiets_Ophalen():
    'User wants to get bike'
    infile = open('nummers.txt', 'r')
    fietsnummer = input('Wat is uw fietsnummer?')
    info = infile.read()
    if fietsnummer in info:
        persoon_info = info.split('\n')
        for ind_info in persoon_info:
            check = str(ind_info).split(',')
            if check[0] == fietsnummer:
                naam = input('Wat is uw naam?')
                wachtwoord = input('Wat is uw wachtwoord?')
                if naam == check[1] and wachtwoord == check[2]:
                    print('Bedankt voor het gebruiken van de NS fietsenstalling')
                    print('de deur is nu open')
                    # Hoe haal ik iets weg uit de txt file
                else:
                    print('Gebruikersnaam of wachtwoord incorrect')
                    print('1: Opnieuw proberen')
                    print('2: Terug naar startscherm')
                    keuze = eval(input('Kies uw optie'))
                    if keuze == 1:
                        Fiets_Ophalen()
                    elif keuze == 2:
                        opties()

    else:
        print('Uw fietsnummer is incorrect.')
        print('1: Opnieuw proberen')
        print('2: Terug naar startscherm')
        keuze = eval(input('Kies uw optie'))
        if keuze == 1:
            opties()
        elif keuze == 2:
            Fiets_Ophalen()


def Fiets_Informatie():
    'User wants to see information, here we tell some basic information and give the user a choice if he/she/it wants to acces personal information'
    print()
    print('Welkom bij de fietsenstalling van de NS. \n' +
          'U kunt uw fiets hier stallen en later weer ophalen, u krijgt een unieke code wat indiceert welke fiets van u is. \n' +
          'Overigens moet u nog een wachtwoord verzinnen.' +
          'Als u persoonlijke informatie wilt moet u zichzelf verificeren.')
    print()
    keuze_info()


def keuze_info():
    'choice making for information catogorie'
    keuze = eval(
        input('Selecteer 0 als u terug naar het hoofdmenu wilt, Selecteer 1 als u bij persoonlijke informatie wilt'))
    while keuze != 0 or keuze != 1:
        if keuze == 0:
            return opties()
        if keuze == 1:
            return Persoonlijke_Info()
        else:
            keuze = eval(input('geef een geldige keuze aub'))


def Persoonlijke_Info():
    'When user selects personal info at Function Keuze_info, you go here'
    fietsnummer = input('Wat is uw nummer?')
    infile = open('nummers.txt', 'r')
    nummer_persoon_wachtwoord = infile.read()
    if fietsnummer in nummer_persoon_wachtwoord:  # Als je fietsnummer bekend is
        organi_nummer_persoon_wachtwoord = nummer_persoon_wachtwoord.split(
            '\n')  # laten we onze chaos lijst ff splitten op regel
        for registraties in organi_nummer_persoon_wachtwoord:  # Voor elke registratie bekend in onze lijst
            lijstje = str(registraties).split(
                ',')  # laten we een mooi lijstje maken van elke registratie, idk why string maar alleen dan deed ie t
            if lijstje[
                0] == fietsnummer:  # zodra we vinden wat de index van onze kandidaat is in onze lijst, onthouden we dit om het te kunnen gebruiken.
                opgegeven_wachtwoord = input(('Hallo {}, Wat is uw wachtwoord?'.format(lijstje[1])))
                if opgegeven_wachtwoord == lijstje[2]:
                    print('WELKOM')  # HIER WIL IK NOG WAT PERSOONLIJKE INFO PLAATSEN OFZO?!?!?!?!!?!?!?!?
                    print('U staat in het systeem sinds {}'.format(lijstje[3]))

    else:
        print('Ongeldig fietsnummer')
        return opties()


def opties():
    'Asks the user for his choice and starts the desired function'
    print('Moguh')
    print('1: Nieuwe fiets registreren')
    print('2: Fiets stallen')
    print('3: Fiets ophalen')
    print('4: Informatie opvragen')
    print('5: Afsluiten')
    keuze = eval(input('Kies uw optie'))
    if keuze == 1:
        Nieuwe_Fiets_Registreren()
    elif keuze == 2:
        Fiets_Stallen()
    elif keuze == 3:
        Fiets_Ophalen()
    elif keuze == 4:
        Fiets_Informatie()
    elif keuze == 5:
        print('Fijne dag verder!')
        return


opties()