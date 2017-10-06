while True:
    woord = input('Doe mij een woord: ')
    if woord == 'stop':
        break
    if woord == 'volgende':
        continue
    print(len(woord))