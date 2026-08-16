import datetime

# timestamp = datetime.datetime.now()
timestamp = datetime.datetime(2020, 1, 1, 15, 55, 20)

print("Timestamp:", timestamp)
print("Year:", timestamp.year)
print("Month:", timestamp.month)
print("Day:", timestamp.strftime("%A"))
