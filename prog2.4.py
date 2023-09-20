# pseudocode

# vraag om de prijs

# vraag om het betaalde bedrag

# haalt prijs van betaalde bedrag

# als waarde negatief is, geef bericht dat waarde te klein is

# gaat door een lijst met bedragen heen om te kijken of het bedrag in de waarde past

# haalt bedrag van waarde af

# print waardes


eurocent = (50, 20, 10, 5, 2, 1)

prijs = int(input("De prijs van het gekozen product: "))
bedrag = int(input("Het betaalde bedrag: "))
print("")

if bedrag > prijs:
    teruggeven = bedrag - prijs
    for x in eurocent:
        aantal = teruggeven // x
        print("aantal munten van " + str(x) + " eurocent is " + str(aantal))
        teruggeven %= x
else:
    print("Het betaalde bedrag is te klein")