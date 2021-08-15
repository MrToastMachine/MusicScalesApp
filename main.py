from tkinter import *
from tkinter import messagebox
import tkinter
import pygame
import json
import time

pygame.init()

FPS = 30
RES = (950, 700)
clock = pygame.time.Clock()
win = pygame.display.set_mode(RES)

#PIANO ATTRIBUTES
sharps = [2,4,7,9,11,14,16,19,21,23] # from C to C
allNotes = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']

class Block():
    components = []
    def __init__(self, x, y, width, height, colour, text=""):
        self.posX = x
        self.posY = y
        self.width = width
        self.height = height
        self.colour = colour
        self.mainText = text
        Block.components.append(self)
    
    @classmethod
    def drawMenu(cls):
        for com in cls.components:
            pygame.draw.rect(win, com.colour, (com.posX, com.posY, com.width, com.height))
            if len(com.mainText) > 0:
                text = myFont.render(com.mainText, 1, colourScheme['buttonText'])
                textPosX = int(RES[0] / 2 - text.get_width() / 2)
                yOffset = 3
                textPosY = int(com.posY + com.height/2 - text.get_height() / 2 + 3)
                win.blit(text, (textPosX, textPosY))


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
    
    def clearHighlights(self):
        for key in self.allKeys:
            key.highlighted = False

    def highlightKey(self, note):
        for key in self.allKeys:
            if key.note.lower() == note:
                key.highlighted = not key.highlighted
    
    def highlightScale(self):
        self.clearHighlights()
        rootPos = allNotes.index(CURRENT_ROOT_NOTE.lower())
        currentScaleArray = allScales[CURRENT_SCALE]

        for i in currentScaleArray:
            notePos = (rootPos + i - 1) % 12
            note = allNotes[notePos]
            self.highlightKey(note)


    def drawWhites(self):
        for key in self.allKeys:
            if not key.isSharp:
                colour = colourScheme['active_key'] if key.highlighted else white 
                pygame.draw.rect(win, colour, (key.xPos, key.yPos, self.keyWidth-2, self.keyHeight))
                text = myFont.render(key.note, 1, black)
                win.blit(text, (key.xPos+15, key.yPos - 30))


    def drawSharps(self):
        for key in self.allKeys:
            if key.isSharp:
                colour = colourScheme['active_key_sharp'] if key.highlighted else black 
                pygame.draw.rect(win, colour, (key.xPos, key.yPos, int(self.keyWidth / 2 + 3), int(self.keyHeight/2 + 10)))
                text = myFont.render(key.note, 1, black)
                win.blit(text, (key.xPos, key.yPos - 50))

    def showKeysInfo(self):
        print("ID", "NOTE")
        for key in self.allKeys:
            print(key.id, key.note, key.xPos)


def ButtonSetup():
    width = 300
    height = 50
    xPos = int((RES[0] / 2) - (width / 2))
    yPos = int(mainMenu.posY + round(mainMenu.height * 0.6))

    return Block(xPos, yPos, width, height, colourScheme['button_bg'], text="Settings")

def buttonPressed(mPos):
    x, y = mPos
    if x > settingsButton.posX and x < settingsButton.posX + settingsButton.width:
        if y > settingsButton.posY and y < settingsButton.posY + settingsButton.height:
            return True
    else: 
        return False

def readInScales():
    with open('jsonScaleStorage.json', 'r') as sFile:
        return json.load(sFile)

def openSettings():

    def addScale(*args):
        global scalesDict, scaleNames, scale

        name = newScaleName.get()
        scaleString = newScaleNotes.get()

        if not name=="" and not scaleString=="":
            try:
                scaleArray = [int(n) for n in scaleString.split(',')]
                oldScales = readInScales()
                oldScales[name] = scaleArray

                with open('jsonScaleStorage.json', 'w') as file:
                    json.dump(oldScales, file)

                scalesDict = readInScales()
                scaleNames = [s for s in scalesDict]
                scale = StringVar(tkWindow, scaleNames[0])

                scaleOptions.update()


                
            except:
                print("That wasnt in the correct format deary")


    def showHelp(*args):
        messagebox.showinfo("Help", "To add a new scale, enter the name of the scale and the notes which make up the scale, with note #1 being the root note")

    def showError(*args):
        print("Not valid Scale")

    def checkValid(*args):
        if not newScaleNotes.get() == "":
            try:
                splitStringArray = [int(n) for n in newScaleNotes.get().split(',')]
                if max(splitStringArray) >= 12 or min(splitStringArray) <= 0:
                    # This is wrong -> ERROR
                    showError()
                else:
                    # Correct -> Remove Error
                    print("Thats good yeah")
            except:
                showError()

    tkWindow = Tk()
    tkWindow.geometry('290x210+500+500')
    tkWindow.title("Scaley")

    scalesDict = readInScales()
    scaleNames = [s for s in scalesDict]
    scale = StringVar(tkWindow, scaleNames[0])


    note = StringVar(tkWindow, allNotes[0])

    newScaleName = StringVar(tkWindow, "")
    newScaleNotes = StringVar(tkWindow, "")
    newScaleNotes.trace('w', checkValid)

    Label(tkWindow, text="Choose Scale:").grid(row=0, column=0, padx=10, pady=10)
    Label(tkWindow, text="Root Note:").grid(row=1, column=0, padx=10)
    Label(tkWindow, text="Add New Scale:").grid(row=2, columnspan=2, padx=10)

    Label(tkWindow, text="Scale Name:").grid(row=3, column=0)
    Label(tkWindow, text="Notes (eg: 1,3,4,5,6):").grid(row=3, column=1)


    scaleOptions = OptionMenu(tkWindow, scale, *scaleNames)
    scaleOptions.grid(row=0, column=1, padx=10)

    noteOptions = OptionMenu(tkWindow, note, *allNotes)
    noteOptions.grid(row=1, column=1, padx=10)

    scaleNameEntry = Entry(tkWindow, textvariable=newScaleName)
    scaleNameEntry.grid(row=4, column=0, padx=10)

    scaleNotesEntry = Entry(tkWindow, textvariable=newScaleNotes)
    scaleNotesEntry.grid(row=4, column=1, padx=10)

    Button(tkWindow, text="Add Scale", command=addScale).grid(row=6,column=0, pady=10)
    Button(tkWindow, text="Help", command=showHelp).grid(row=6,column=1)
    Button(tkWindow, text="Done", command=tkWindow.destroy).grid(row=7,columnspan=2)


    mainloop()

def drawFrame():
    win.fill(colourScheme['background'])

    myKeyboard.drawWhites()
    myKeyboard.drawSharps()
    
    Block.drawMenu()

    pygame.display.update()

def cycleColour(section):
    current = colourScheme[section]
    newIndex = allColours.index(current)

#COLOURS
white = (255, 255, 255)
black = (  0,   0,   0)
dark_teal = (38, 70, 83)
light_teal = (42, 157, 143)
yellow = (233, 196, 106)
orange = (244, 162, 97)
red_orange = (231, 111, 81)

allColours = [
    white,
    black,
    dark_teal,
    light_teal,
    yellow,
    orange,
    red_orange
]

colourScheme = {
    "mainMenu": yellow,
    "background": red_orange,
    "buttonText": white,
    "button_bg": light_teal,
    "active_key": light_teal,
    "active_key_sharp": yellow
}

#FONT SETUP
myFont = pygame.font.SysFont('Bookman', 40)

myKeyboard = Keyboard()
mainMenu = Block(0, 500, RES[0], RES[1] - 500, colourScheme['mainMenu'])
settingsButton = ButtonSetup()


allScales = readInScales()
CURRENT_ROOT_NOTE = "C"
CURRENT_SCALE = "Major"

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if buttonPressed(mousePos):
                openSettings()
        elif event.type == pygame.KEYDOWN:
            if allNotes.count(event.unicode.lower()) >= 1:
                # myKeyboard.highlightKey(event.unicode)
                print(CURRENT_ROOT_NOTE)
                CURRENT_ROOT_NOTE = event.unicode
                print(CURRENT_ROOT_NOTE)
            elif event.unicode == 'p':
                myKeyboard.highlightScale()
    drawFrame()
        
"""
Thoughts:
- Be able to choose major or minor scale
- Choose root note and all others in scale get highlighted
- Number all notes in key
- Create new scale feature (Enter numbers for each note in scale)

- Later... Add in chord mode to display chords
    + 1st, 3rd and 5th etc...
- Much much later >> Show notes on guitar frets
"""
