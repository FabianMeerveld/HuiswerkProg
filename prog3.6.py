s = "Guido van Rossum heeft programmeertaal Python bedacht."

for letter in s.lower():
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        print(letter)
