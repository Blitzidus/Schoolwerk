cijferICOR = 6
cijferPROG = 8
cijferCSN = 7

cijferTotaal = cijferCSN + cijferICOR + cijferPROG

gemiddelde = round(cijferTotaal / 3, 1)
beloning = 30 * cijferTotaal
overzicht = 'Mijn cijfer (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van € ' + str(beloning) + ' op!'

print(overzicht)
