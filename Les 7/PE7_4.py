def getAllTickers(filename):
    with open(filename, "r", encoding="utf-8") as file:
        tickers = {}
        data = file.read().splitlines()
        for line in data:
            splitData = line.split(":")
            tickers[splitData[0]] = splitData[1]
        return tickers


def searchForTicker(companyName):
    tickers = getAllTickers("ticker-symbol.txt")
    for tick in tickers.items():
        if (tick[0] == companyName):
            print("Ticker symbol: {}".format(tick[1]))


def searchForCompanyName(ticker):
    tickers = getAllTickers("ticker-symbol.txt")
    for tick in tickers.items():
        if (tick[1] == ticker):
            print("Company name: {}".format(tick[0]))


searchForTicker(input("Enter Company name: "))
searchForCompanyName(input("Enter Ticker symbol: "))
