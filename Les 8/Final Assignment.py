def inlezen_beginstation(stations):
    while True:
        beginstation = input('Wat is uw beginstation? ')
        if beginstation in stations:
            return beginstation
        else:
            print('Uw ingetoetste station is incorrect.')


def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input('Wat is uw eindstation? ')
        if eindstation in stations:

            if stations.index(eindstation) > stations.index(beginstation):
                return eindstation
            else:
                 print('De trein rijdt niet achteruit. ')
        else:
            print('Uw ingetoetste station is incorrect.')

def omroepen_reis(stations, beginstation, eindstation):
    index_begin_station = stations.index(beginstation)
    index_eind_station = stations.index(eindstation)
    print('Het beginstation ' + str(beginstation) + 'is het ' + str(
        stations.index(beginstation) + 1) + 'e station in het traject.')
    print('Het eindstation ' + str(eindstation) + 'is het ' + str(
        stations.index(eindstation) + 1) + 'e station in het traject.')
    print('De afstand bedraagt ' + str(stations.index(eindstation) - stations.index(beginstation)) + ' stations')
    print('De prijs van het kaartje is ', str(5 * (stations.index(eindstation) - stations.index(beginstation))))
    print('Jij stapt in op station: ' + (beginstation))
    print('De tussenliggende stations zijn: ')
    for tussenliggendestations in stations[index_begin_station + 1: index_eind_station]:
        print('-', tussenliggendestations, )
    print('Jij stapt uit in: ' + (eindstation))


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
