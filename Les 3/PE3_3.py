leeftijd = eval(input('Geef uw leeftijd '))
paspoort = (input('Heeft u een paspoort? '))
if leeftijd >= 18 and paspoort == 'ja' :
    print('U mag stemmen')
else:
    print('U mag niet stemmen')