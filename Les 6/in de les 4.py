afstandKM = [-1, 10, 50, 100]
weekend = [True, False]
leeftijd = [5, 11, 25, 65, 80]

for km in afstandKM:
    for dag in weekend:
        for age in leeftijd:
            ritprijs(km, dag, age)