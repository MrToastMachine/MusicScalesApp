import json
import pygame

pygame.font.init()
FONT = pygame.font.SysFont(None, 50)

ALL_NOTES = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']

ACTIVE_ROOT = None
ACTIVE_SCALE = None

scales = {}

def getFont(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def readInScales():
    with open('jsonScaleStorage.json', 'r') as sFile:
        json_scales = json.load(sFile)
        for scale in json_scales:
            scales[scale] = json_scales[scale]
    
def getNotesInScale(root, scale):
    notes_in_scale = []
    root_pos = ALL_NOTES.index(root)
    for note_pos in scale:
        note_index = (root_pos + note_pos - 1) % len(ALL_NOTES)
        notes_in_scale.append(ALL_NOTES[note_index])
    
    return(notes_in_scale)

