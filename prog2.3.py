uurloon = input("Wat is uw uurloon? \n")
aantal_uur = input("Hoeveel uur heeft u gewerkt? \n")

text = "Wat verdien je per uur: " + uurloon + "\nHoeveel uur heb je gewerkt: " + aantal_uur + "\n" + aantal_uur + " uur werken levert €" + str(
    float(uurloon) * float(aantal_uur)) + " op"

print(text)
