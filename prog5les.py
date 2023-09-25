events = '9/13 2:30 PM\n9/14 11:15 AM\n9/14 1:00 PM\n9/15 9:00 AM'

print(events.count("9/14"))
print(events.find("9/14"))
print(events.find("9/15"))
print(events[events.find("9/14"):events.find("9/15")].strip().split("\n"))


