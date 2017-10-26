invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
numbers = invoer.split("-")
numbers = list(map(int, numbers))
numbers.sort()
print("Gesorteerde list van ints: {}".format(numbers))
print("Grootste getal: {} en Kleinste getal: {}".format(numbers[-1], numbers[0]))
print("Aantal getallen: {} en Som van de getallen: {}".format(len(numbers), sum(numbers)))
print("Gemiddelde: {}".format(sum(numbers) / len(numbers)))
