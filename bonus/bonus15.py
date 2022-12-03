import json

with open("files/questions.json", 'r') as file:
    data = json.load(file)

print(data)

