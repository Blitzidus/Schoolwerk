while True:
    letters = input("Geef een string van vier letters: ")
    if len(letters) == 4:
        print("lezen van correcte string: {} is geslaagd".format(letters))
        break
    else:
        print("{} heeft {} letters\n".format(letters, len(letters)))
