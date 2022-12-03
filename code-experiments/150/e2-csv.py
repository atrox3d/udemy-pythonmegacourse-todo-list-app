import csv

with open("files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

print(data)

for row in data:
    city, temperature = row
    print(city, temperature)