import json

with open('jsonScaleStorage.json', 'r') as file:
    data = json.load(file)
    for element in data:
        print(element, data[element])