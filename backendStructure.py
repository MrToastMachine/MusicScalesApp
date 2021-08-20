import pygame
import json

def readInScales():
    with open('jsonScaleStorage.json', 'r') as sFile:
        return json.load(sFile)

class Key():
    def __init__(self, id, note, xPos, yPos, isSharp):
        self.id = id
        self.note = note
        self.xPos = xPos
        self.yPos = yPos
        self.isSharp = isSharp
        self.highlighted = False

        
class Keyboard():
    def __init__(self, win, font):
        self.xOffset = 100
        self.yOffset = 100
        self.keyWidth = 50
        self.keyHeight = 300
        self.allKeys = []
        self.win = win
        self.font = font
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
    
    def clearHighlights(self):
        for key in self.allKeys:
            key.highlighted = False

    def highlightKey(self, note):
        for key in self.allKeys:
            if key.note.lower() == note:
                key.highlighted = not key.highlighted
    
    def highlightScale(self, root, scale):
        self.clearHighlights()
        rootPos = allNotes.index(root.lower())
        currentScaleArray = allScales[scale]

        print(root, scale)

        for i in currentScaleArray:
            notePos = (rootPos + i - 1) % 12
            note = allNotes[notePos]
            self.highlightKey(note)


    def drawWhites(self):
        for key in self.allKeys:
            if not key.isSharp:
                colour = colourScheme['active_key'] if key.highlighted else white 
                pygame.draw.rect(self.win, colour, (key.xPos, key.yPos, self.keyWidth-2, self.keyHeight))
                text = self.font.render(key.note, 1, black)
                labelPosX = round(key.xPos + (self.keyWidth/2) - (text.get_width()/2))
                labelPosY = key.yPos + self.keyHeight - 35
                self.win.blit(text, (labelPosX, labelPosY))


    def drawSharps(self):
        for key in self.allKeys:
            if key.isSharp:
                colour = colourScheme['active_key_sharp'] if key.highlighted else black 
                pygame.draw.rect(self.win, colour, (key.xPos, key.yPos, int(self.keyWidth / 2 + 3), int(self.keyHeight/2 + 10)))
                text = self.font.render(key.note, 1, black)
                self.win.blit(text, (key.xPos, key.yPos - 35))

    def showKeysInfo(self):
        print("ID", "NOTE")
        for key in self.allKeys:
            print(key.id, key.note, key.xPos)


#PIANO ATTRIBUTES
sharps = [2,4,7,9,11,14,16,19,21,23] # from C to C
allNotes = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']

#COLOURS
white = (255, 255, 255)
black = (  0,   0,   0)
dark_teal = (38, 70, 83)
light_teal = (42, 157, 143)
yellow = (233, 196, 106)
orange = (244, 162, 97)
red_orange = (231, 111, 81)

colourScheme = {
    "mainMenu": light_teal,
    "background": red_orange,
    "buttonText": white,
    "button_bg": yellow,
    "active_key": light_teal,
    "active_key_sharp": yellow
}

allScales = readInScales()
