import pygame
from keyboardVisualiser import *

CURRENT_ROOT_NOTE = "C"
CURRENT_SCALE = "Major"

class Block():
    components = []
    def __init__(self, win, x, y, width, height, colour, font=None, text=""):
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.font = font
        self.text = text
        Block.components.append(self)

    @classmethod
    def drawMenu(cls):
        for com in cls.components:
            pygame.draw.rect(com.win, com.colour, (com.x, com.y, com.width, com.height))
            if len(com.text) > 0:
                text = com.font.render(com.text, 1, colourScheme['buttonText'])
                textx = int(com.x + com.width/2 - text.get_width() / 2)
                yOffset = 3
                texty = int(com.y + com.height/2 - text.get_height() / 2 + 3)
                com.win.blit(text, (textx, texty))

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

class Button(Block):
    all_buttons = []

    def __init__(self, win,  x, y, width, height, colour, func, font=None, text=""):
        Block.__init__(self, win, x, y, width, height, colour, font, text)
        self.func = func
        Button.all_buttons.append(self)

    def setRootNote(self):
        CURRENT_ROOT_NOTE = self.text
        print(f"[Button] Setting Root Note to :: {self.text}")
        print(f"New CURRENT_ROOT_NOTE: {CURRENT_ROOT_NOTE}")

    @classmethod
    def checkClicked(cls, mousePos):
        for button in cls.all_buttons:
            if mousePos[0] >= button.x and mousePos[0] <= button.x + button.width:
                if mousePos[1] >= button.y and mousePos[1] <= button.y + button.height:
                    button.func(button)
