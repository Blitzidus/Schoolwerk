import xmltodict

xmlFile = "infodata.xml"


def getXMLData(filename):
    with open(filename, "r")as file:
        data = file.read()
        return xmltodict.parse(data)


xmlDictionaryData = getXMLData(xmlFile)

for product in xmlDictionaryData['artikelen']['artikel']:
    print(product['naam'])
