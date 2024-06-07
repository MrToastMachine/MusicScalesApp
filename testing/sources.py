import json

scales = {}

def readInScales():
    with open('jsonScaleStorage.json', 'r') as sFile:
        json_scales = json.load(sFile)
        for scale in json_scales:
            scales[scale] = json_scales[scale]
    

