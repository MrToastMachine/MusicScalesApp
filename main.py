from typing import overload
import pygame
import time

pygame.init()

FPS = 30
RES = (950, 700)
clock = pygame.time.Clock()
win = pygame.display.set_mode(RES)

#COLOURS
white = (255, 255, 255)
black = (  0,   0,   0)
almost_black = (0, 18, 25)
orange = (231, 111, 81)
yellow = (255, 255, 0)

#PIANO ATTRIBUTES
sharps = [2,4,7,9,11,14,16,19,21,23] # from C to C
allNotes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

class Key():
    def __init__(self, id, note, xPos, yPos, isSharp):
        self.id = id
        self.note = note
        self.xPos = xPos
        self.yPos = yPos
        self.isSharp = isSharp
        self.highlighted = False

        
class Keyboard():
    def __init__(self):
        self.xOffset = 100
        self.yOffset = 100
        self.keyWidth = 50
        self.keyHeight = 300
        self.allKeys = []
        self.createKeyboard()
    
    def createKeyboard(self):
        lastNoteSharp = False
        whiteNoteOffset = 0
        sharpNoteOffset = 1
        for i in range(25):
            isSharp = sharps.count(i+1) >= 1
            yPos = self.yOffset
            note = allNotes[i % 12]
            if isSharp:
                xPos = self.xOffset + ((i-sharpNoteOffset)*self.keyWidth) + 35
                lastNoteSharp = True
                sharpNoteOffset += 1
            else:
                whiteNoteOffset = whiteNoteOffset + 1 if lastNoteSharp else whiteNoteOffset
                xPos = self.xOffset + (i-whiteNoteOffset)*self.keyWidth
                
                lastNoteSharp = False

            newKey = Key(i+1, note, xPos, yPos, isSharp)
            self.allKeys.append(newKey)
    
    def highlightKey(self, note):
        for key in self.allKeys:
            if key.note.lower() == note:
                key.highlighted = not key.highlighted
                print(f"ID: {key.id}")
    
    def drawWhites(self):
        for key in self.allKeys:
            if not key.isSharp:
                colour = yellow if key.highlighted else white 
                pygame.draw.rect(win, colour, (key.xPos, key.yPos, self.keyWidth-2, self.keyHeight))

    def drawSharps(self):
        for key in self.allKeys:
            if key.isSharp:
                colour = yellow if key.highlighted else black 
                pygame.draw.rect(win, colour, (key.xPos, key.yPos, self.keyWidth / 2 + 3, self.keyHeight/2 + 10))

    def showKeysInfo(self):
        print("ID", "NOTE")
        for key in self.allKeys:
            print(key.id, key.note, key.xPos)

def drawFrame():
    win.fill(orange)

    myKeyboard.drawWhites()
    myKeyboard.drawSharps()

    pygame.display.update()


myKeyboard = Keyboard()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if allNotes.count(event.unicode.upper()) >= 1:
                myKeyboard.highlightKey(event.unicode)
            elif event.unicode == 'p':
                myKeyboard.showKeysInfo()
    drawFrame()
        
"""
Thoughts:
- Be able to choose major or minor scale
- Choose root note and all others in scale get highlighted
- Number all notes in key
- Create new scale feature (Enter numbers for each note in scale)

- Later... Add in chord mode to display chords
- Much much later >> Show notes on guitar frets
"""
