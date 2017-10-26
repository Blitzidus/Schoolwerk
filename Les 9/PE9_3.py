import csv
from pathlib import Path

filename = "HighscoreData.csv"

def GetHigestScoreDataFromCSV(bestand):
    if Path(bestand).is_file():
        highestData = ["", "", ""]
        with open(bestand, 'r') as file:
            for row in csv.reader(file):
                data = str(row[0]).split(";")
                if highestData[2] < data[2]:
                    highestData = data
            return highestData
    else:
        print('no file found')


highscoreData = GetHigestScoreDataFromCSV(filename)

print(
    "De highscore is: {} op {} en is gehaald door {}".format(highscoreData[2], highscoreData[1], highscoreData[0]))
