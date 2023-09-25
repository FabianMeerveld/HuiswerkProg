import datetime


def write_file(name):
    today = datetime.datetime.today()
    date = today.strftime("%a %d %b %Y, %H:%M:%S")
    file = open("pe_5_4_hardlopers.txt", "a")
    file.write(f'{date}, {name}\n')
    file.close()


while True:
    text = input("Wat is de naam: ")
    write_file(text)
