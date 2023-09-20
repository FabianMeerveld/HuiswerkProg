from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")

print(formatted_datetime)