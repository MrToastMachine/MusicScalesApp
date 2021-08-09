import json

with open('jsonScaleStorage.json', 'r') as file:
    data = json.load(file)
    names = [s for s in data]
    print(names[0])