maand = int(input("Geef een maandnummer: "))

if 3 <= maand <= 5:
    print("lente")
elif 9 <= maand <= 11:
    print("herfst")
elif 6 <= maand <= 8:
    print("zomer")
elif maand == 12 or 1 <= maand <=2:
    print("winter")
else:
    print("ongeldig")
