studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(studentencijfers):
    middleNumberPerson = []
    for studentlist in studentencijfers:
        middleNumberPerson.append(round(sum(studentlist) / len(studentlist)))
    return middleNumberPerson


def gemiddelde_van_alle_studenten(studentencijfers):
    middleNumberPersons = gemiddelde_per_student(studentencijfers)
    return round(sum(middleNumberPersons) / len(middleNumberPersons))


print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
