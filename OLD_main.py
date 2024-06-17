import pygame
import json
from backendStructure import *
import tkSettingsWindow as settings

pygame.init()

FPS = 30
RES = (1000, 700)
clock = pygame.time.Clock()
win = pygame.display.set_mode(RES)


def ButtonSetup(xPos, yPos, text):
    width = 300
    height = 50

    return Block(win, xPos, yPos, width, height, colourScheme['button_bg'], buttonFont, text=text)

def buttonPressed(mPos):
    x, y = mPos
    if x > settingsButton.posX and x < settingsButton.posX + settingsButton.width:
        if y > settingsButton.posY and y < settingsButton.posY + settingsButton.height:
            return True
    else: 
        return False

def drawFrame():
    win.fill(colourScheme['background'])

    myKeyboard.drawWhites()
    myKeyboard.drawSharps()
    
    Block.drawMenu()
    TextDisplay.drawAllText()

    pygame.display.update()

#FONT SETUP
buttonFont = pygame.font.SysFont('Aldhabi', 40)
titleFont = pygame.font.SysFont('Aldhabi', 40)
textFont = pygame.font.SysFont('Aldhabi', 40)

scaleHeading = TextDisplay(win, 130, 530, titleFont, "Current Scale")
rootNoteHeading = TextDisplay (win, 600, 530, titleFont, "Current Root Note")

myKeyboard = Keyboard(win, buttonFont)
mainMenu = Block(win, 0, 500, RES[0], RES[1] - 500, colourScheme['mainMenu'])
settingsButton = ButtonSetup(80, 620, "Settings")
controlsButton = ButtonSetup(570, 620, "Controls")


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
                settings.openSettings()
        elif event.type == pygame.KEYDOWN:
            if ALL_NOTES.count(event.unicode.lower()) >= 1:
                print(CURRENT_ROOT_NOTE)
                CURRENT_ROOT_NOTE = event.unicode
                print(CURRENT_ROOT_NOTE)
                myKeyboard.highlightScale(CURRENT_ROOT_NOTE, CURRENT_SCALE)
            elif event.unicode == 'p':
                myKeyboard.highlightScale(CURRENT_ROOT_NOTE, CURRENT_SCALE)
            elif event.key == pygame.K_SPACE:
                myKeyboard.showScale = not myKeyboard.showScale                
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
