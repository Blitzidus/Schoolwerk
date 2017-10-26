print("Wat is je uurloon?")
hourPayment = int(input())
print("Aantal uren gewerkt?")
hourAmount = int(input())

totalPayment = hourAmount * hourPayment

print("Wat verdien je per uur: " + str(hourPayment))
print("Hoeveel uur heb je gewerkt: " + str(hourAmount))
print(str(hourAmount) + " uur werken levert € " + str(totalPayment) + " op")
