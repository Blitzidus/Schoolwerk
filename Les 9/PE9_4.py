import csv
import os
from decimal import Decimal

articleFile = "artikelbestand.csv"

csvdata = [
    ["Artikelnummer", "Actikelcode", "Naam", "Voorraad", "Prijs"],
    ["121", "ABC123", "Highlight pen", "231", "0.56"],
    ["123", "PQR678", "Nietmachine", "587", "9.99"],
    ["128", "ZYX163", "Bureaulamp", "34", "19.95"],
    ["137", "MLK709", "Monitorstandaard", "66", "32.50"],
    ["273", "TRS665", "Ipad hoes", "55", "19.01"],
]


def writeArticlesToCsv(path, data):
    if not os.path.isfile(path):
        with open(path, 'w', newline='') as file:
            csvwriter = csv.writer(file, delimiter=";")
            for row in data:
                csvwriter.writerow(row)


def readArticleToCsv(path, delimiter=";"):
    if os.path.isfile(path):
        with open(path, 'r', newline='') as file:
            data = csv.reader(file)
            next(data)
            subdata = []
            for line in data:
                subdata.append(str(line[0]).split(delimiter))
            return subdata


def getArticleById(data, id):
    for product in data:
        if int(product[0]) == id:
            return product


def checkArticles(data):
    highPriceArticleId = 0
    highPriceArticlePrice = 0
    totalProducts = 0
    for product in data:
        totalProducts += int(product[3])

        if (highPriceArticlePrice < float(product[4])):
            highPriceArticlePrice = float(product[4])
            highPriceArticleId = int(product[0])

    articleData = getArticleById(data, highPriceArticleId)
    print('Het duurste artikel is {} want die kost {} Euro'.format(articleData[2], Decimal(articleData[4])))
    print('Er zijn {} exemplaren in voorraad van het product met nummer {}'.format(articleData[3],
                                                                                           articleData[0]))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totalProducts))


writeArticlesToCsv(articleFile, csvdata)
data = readArticleToCsv(articleFile)
checkArticles(data)
