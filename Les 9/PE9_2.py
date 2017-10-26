import datetime
import csv
from pathlib import Path

bestand = 'inloggegevens.csv'
fieldNames = ['date', 'lname', 'fletters', 'birthDate', 'email']


def CheckCSV(bestand, fieldNames):
    if not Path(bestand).is_file():
        with open(bestand, 'w') as file:
            CSVwriter = csv.DictWriter(file, fieldnames=fieldNames, delimiter=';')
            CSVwriter.writeheader()


def WriteToCSV(bestand, fieldNames, dataDict):
    with open(bestand, 'a') as file:
        CSVwriter = csv.DictWriter(file, fieldnames=fieldNames, delimiter=';')
        CSVwriter.writerow(dataDict)


while True:
    date = datetime.datetime.now().strftime("%a %d %b %Y at %H:%M")
    naam = input("Wat is je achternaam? ")
    if naam == 'einde' or naam == '':
        exit()
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je email adres? ")

    dataDict = {'date': date, 'lname': naam, 'fletters': voorl, "birthDate": gbdatum, "email": email}
    CheckCSV(bestand, fieldNames)
    WriteToCSV(bestand, fieldNames, dataDict)
