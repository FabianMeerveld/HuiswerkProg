file = open("TestFile.txt", "a")

file.write("Fabian Meerveld\n")

file.close()

file = open("TestFile.txt", "r")
print(file.readlines())
