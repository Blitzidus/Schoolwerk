def namen():
    students = {}
    givenName = ""
    while givenName != "" or len(students) < 1:
        givenName = input("Volgende naam: ")

        if givenName in students.keys():
            students[givenName] += 1
        elif givenName != "":
            students[givenName] = 1
    for student in students.items():
        if (student[1] == 1):
            print("Er is {} student met de naam {}".format(student[1], student[0]))
        else:
            print("Er zijn {} studenten met de naam {}".format(student[1], student[0]))


namen()
