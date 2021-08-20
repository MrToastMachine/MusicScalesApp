from sys import winver
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
        self.showScale = False
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
                colour = colourScheme['active_key'] if key.highlighted and self.showScale else white 
                pygame.draw.rect(self.win, colour, (key.xPos, key.yPos, self.keyWidth-2, self.keyHeight))
                text = self.font.render(key.note, 1, black)
                labelPosX = round(key.xPos + (self.keyWidth/2) - (text.get_width()/2))
                labelPosY = key.yPos + self.keyHeight - 35
                self.win.blit(text, (labelPosX, labelPosY))


    def drawSharps(self):
        for key in self.allKeys:
            if key.isSharp:
                colour = colourScheme['active_key_sharp'] if key.highlighted and self.showScale else black 
                pygame.draw.rect(self.win, colour, (key.xPos, key.yPos, int(self.keyWidth / 2 + 3), int(self.keyHeight/2 + 10)))
                text = self.font.render(key.note, 1, black)
                self.win.blit(text, (key.xPos, key.yPos - 35))

class Block():
    components = []
    def __init__(self, win, x, y, width, height, colour, font=None, text=""):
        self.win = win
        self.posX = x
        self.posY = y
        self.width = width
        self.height = height
        self.colour = colour
        self.font = font
        self.mainText = text
        Block.components.append(self)

    @classmethod
    def drawMenu(cls):
        for com in cls.components:
            pygame.draw.rect(com.win, com.colour, (com.posX, com.posY, com.width, com.height))
            if len(com.mainText) > 0:
                text = com.font.render(com.mainText, 1, colourScheme['buttonText'])
                textPosX = int(com.posX + com.width/2 - text.get_width() / 2)
                yOffset = 3
                textPosY = int(com.posY + com.height/2 - text.get_height() / 2 + 3)
                com.win.blit(text, (textPosX, textPosY))

class TextDisplay():
    allTexts = []
    def __init__(self, win, x, y, font, text):
        self.win = win
        self.xPos = x
        self.yPos = y
        self.font = font
        self.text = text
        TextDisplay.allTexts.append(self)

    @classmethod
    def drawAllText(cls):
        for label in cls.allTexts:
            text = label.font.render(label.text, 1, colourScheme['menuText'])
            label.win.blit(text, (label.xPos, label.yPos))


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
    "buttonText": dark_teal,
    "menuText": white,
    "button_bg": yellow,
    "active_key": light_teal,
    "active_key_sharp": yellow
}

allScales = readInScales()
