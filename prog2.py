import math

c = math.sqrt(3**2+4**2)
print(c)
c = c == 5
print(c)
c = math.pi*10**2
print(c)
c = 5**2+5**2 < 7**2
print(c)

naam = input("Naam: ")
leeftijd = int(input("Leeftijd: "))
tekst = naam + ", volgend jaar ben jij " + str(leeftijd + 1) + " jaar oud!"
print(tekst)

if leeftijd >= 18:
    print(naam + " mag stemmen!")
else:
    print(naam + " mag nog niet stemmen, probeer over " + str(18 - leeftijd) + " jaar opnieuw!")
