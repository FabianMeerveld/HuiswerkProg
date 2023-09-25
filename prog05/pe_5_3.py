file = open("pe_5_2_generated.txt")
lines = file.readlines()
file.close()

print(f'Deze file telt {len(lines)} regels')

biggestline = ""
biggestnumber = 0
for x in lines:
    if int(x.split(",")[0]) > biggestnumber:
        biggestnumber = int(x.split(",")[0])
        biggestline = x

index = lines.index(biggestline)+1

print(f'Het grootste kaartnummer is: {str(biggestnumber)} en dat staat op regel {str(index)}')

