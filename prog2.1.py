cijferPROJA = 8
cijferPROG = 7
cijferMOD = 8

gemiddelde = (cijferMOD+cijferPROG+cijferPROJA) / 3

beloning = 30*3*gemiddelde

overzicht = "Bijvoorbeeld: 'Mijn cijfers (gemiddeld een " + str(gemiddelde) + ") leveren een beloning van € " + str(beloning) + " op!"
print(overzicht)
