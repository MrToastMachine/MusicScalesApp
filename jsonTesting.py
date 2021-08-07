import json



data = {
    "Major": [1,3,5,6,8,10,12],
    "Minor": [1,3,4,6,8,9,11]
}
tempFile = "jsonScaleStorage.json"
with open(tempFile, 'w') as file:
    json.dump(data, file)
