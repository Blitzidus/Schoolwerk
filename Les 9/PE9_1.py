def CalculatePerPerson():
    try:
        peopleAmount = int(input("Enter the amount of people: "))
        priceInEuro = 4356
        if peopleAmount < 0:
            raise Exception

        totalAPerson = priceInEuro / peopleAmount
        print(round(totalAPerson, 2))
    except ZeroDivisionError:
        print("Delen door nul kan niet.")
    except ValueError:
        print("Voor het invoeren van het aantal zijn cijfers vereist.")
    except Exception:
        print("Negatieve getallen mogen niet.")
    except:
        print("Onjuiste invoer.")


while True:
    CalculatePerPerson()
