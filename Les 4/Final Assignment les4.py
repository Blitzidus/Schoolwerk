def standaardprijs(afstandKM):
    if afstandKM <= 0:
        return (0)
    if afstandKM >= 50:
        return (15 + (afstandKM * 0.6))
    else:
        return (afstandKM * 0.8)

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd > 64:
         if weekendrit == True:
            prijs = standaardprijs(afstandKM) * 0.65
         else:
            prijs = standaardprijs(afstandKM) * 0.7
    else:
        if weekendrit == True:
            prijs = standaardprijs(afstandKM) * 0.6
        else:
            prijs = standaardprijs(afstandKM)
    return prijs

afstandKM = [-1, 10, 50, 100]
weekendrit = [True, False]
leeftijd = [5, 11, 25, 65, 80]

print(ritprijs(12, True, -1))
for age in leeftijd:
    for dag in weekendrit:
        for km in afstandKM:
           resultaat = ritprijs(age, dag, km)
           print(resultaat)

